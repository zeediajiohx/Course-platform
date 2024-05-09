// pages/wxlogin/wxlogin.js
var app = getApp();

var api = require('../../config/api.js')
Page({
    /**
     * 页面的初始数据
     */
    data: {
        info:{},
        userInfo: {},
        hasUserInfo: false,
        token:null,
        phone:null,
        canIUseGetUserProfile: false,
        // manag:false,
        tags:['computer science','senion math'],
        commuinum:{"粉丝":0,"关注":0,"点赞收藏":0,},

        minID : 0,
      maxID : 0,
      classlist:[],
      classlist1:[],
      pagestatus:0,
      navigturl:"/pages/imagenews/imagenews?videoID"
    },
    swipstatus:function(e){
        this.setData({
            pagestatus:e.detail.current
        })
        if(this.data.pagestatus==0){
            this.tomyrecord()
            
        }else if(this.data.pagestatus==1){
            this.tomyfavor()
            this.setData({
                
            })
        }else if(this.data.pagestatus==2){
            this.tomycollect()
            this.setData({
               
            })
        }
    },
    tomyrecord:function(){
        this.setData({
            pagestatus:0,
            navigturl:"/pages/imagenews/imagenews?videoID"
          
        })
        this.loaddata(api.myrecord)
    },
    tomyfavor:function(){
        this.setData({
            pagestatus:1,
            navigturl:"/pages/video/video?videoID"
        })
        this.loaddata(api.myfavor)
    },
    tomycollect:function(){
        this.setData({
            pagestatus:2,
            navigturl:"/pages/video/video?videoID"
        })
        this.loaddata(api.mycollect)
    },
    loaddata:function(url){
        if(this.data.info.token){
            wx.request({
                url: url,
                dataType: 'json',
                method: 'GET',
                header:{
                    Authorization: this.data.info.token?this.data.info.token: null
                  },
                responseType: 'text',
                success: (result) => {
                  console.log(result)
                  
                  //最大和最小ID
                  var cls = []
                  var cls1 = []
                  for (var i=0;i<result.data.length;i++){
                    if(i%2==0){
                      cls.push(result.data[i])
                    }else{
                      cls1.push(result.data[i])
                    }
                  }
                  console.log('mycls1',cls1,'mycls',cls)
                  if(result.data.length>0){
                    this.setData({
                        classlist:cls,
                        classlist1:cls1,
                        minID:result.data[result.data.length-1].videoID,
                        maxID:result.data[0].videoID
                      })
                  }
                  else{
                      this.setData({
                        classlist:cls,
                        classlist1:cls1,
                      })
                  }
                  
                },
                fail: (res) => {
                  console.log('fail',api.indexURL)
                },
                complete: (res) => {},
              })
        }
    },
    loadpulldata:function(url){
        wx.request({
            url:url,
            data: {max_id : this.data.maxID},
            dataType: 'json',
            method: 'GET',
            responseType:'text',
            header:{
                Authorization: this.data.info?this.data.info.token: null
              },
            success: (result) => {
              if(!result.data.length){
                wx.showToast({
                  title: 'No more!',
                  icon:'loading',
                })
                wx.stopPullDownRefresh()
                return
              }
              console.log(result);
              if(result.data.length){
              var dataList = result.data.reverse();
              var cls = []
              var cls1 = []
              for (var i=0;i<dataList.length;i++){
                if(i%2==0){
                  cls.push(dataList[i])
                }else{
                  cls1.push(dataList[i])
                }
              }
              console.log('cls1',cls1,'cls',cls)}
              this.setData({
                classlist:cls.concat(this.data.classlist),
                classlist1:cls1.concat(this.data.classlist1),
                maxID:dataList[0].videoID,
                
              })
            },
            fail: (res) => {
                wx.showToast({
                  title: '请先登录',
                  
                })
            },
            complete: (res) => {},
          })

    },
    loadbottomdata:function(url){
        wx.request({
            url: url,
            data: {min_id : this.data.minID},
            header:{
                Authorization:this.data.info.token?this.data.info.token: null
              },
            dataType: 'json',
            method: 'GET',
            responseType:'text',
            success: (result) => {
              if(!result.data.length){
                wx.showToast({
                  title: 'No more!',
                  icon:'loading',
                })
                return
              }
              console.log(result);
              var cls = []
              var cls1 = []
              for (var i=0;i<result.data.length;i++){
                if(i%2==0){
                  // console.log(result.data[i].videoID)
                  cls.push(result.data[i])
                }else{
                  // console.log(result.data[i].videoID)
                  cls1.push(result.data[i])
                }
              }
              console.log('cls1',cls1,'cls',cls)
              this.setData({
                classlist:this.data.classlist.concat(cls),
                classlist1:this.data.classlist1.concat(cls1),
                minID:result.data[result.data.length-1].videoID
              })
            },
            fail: (res) => {
                wx.showToast({
                  title: '请先登录',
                })
            },
            complete: (res) => {},
          })
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

        if (wx.getUserProfile) {
            this.setData({
              canIUseGetUserProfile: true
            })
          }
          this.setData({
              tags:[wx.getStorageSync('academy')?wx.getStorageSync('academy'):"ComputerScience",wx.getStorageSync('major')?wx.getStorageSync('major'):"Big Data"],
              info:wx.getStorageSync('userInfo'),
            //   manag:this.info.ismanager
          })
        //   console.log('manag?',this.data.manag)
        if(this.data.pagestatus==0){
            this.tomyrecord()
        }else if(this.data.pagestatus==1){
            this.tomyfavor()
        }else if(this.data.pagestatus==2){
            this.tomycollect()
        }
        // if(this.data.info){
        //     wx.request({
        //         url: api.myrecord,
        //         dataType: 'json',
        //         method: 'GET',
        //         header:{
        //             Authorization: this.data.info?this.data.info.token: null
        //           },
        //         responseType: 'text',
        //         success: (result) => {
        //           console.log(result)
        //           //最大和最小ID
        //           var cls = []
        //           var cls1 = []
        //           for (var i=0;i<result.data.length;i++){
        //             if(i%2==0){
        //               cls.push(result.data[i])
        //             }else{
        //               cls1.push(result.data[i])
        //             }
        //           }
        //           console.log('mycls1',cls1,'mycls',cls)
        //           this.setData({
        //             classlist:cls,
        //             classlist1:cls1,
        //             minID:result.data[result.data.length-1].videoID,
        //             maxID:result.data[0].videoID
        //           })
        //         },
        //         fail: (res) => {
        //           console.log('fail',URL.indexURL)
        //         },
        //         complete: (res) => {},
        //       })
        // }
        //标签
          var that = this;

          
          
    },
    getUserProfile(e) {
      var app = getApp()
        var that = this;
        wx.getUserProfile({
          desc: '用于完善会员资料', 
          success: (res) => {
              console.log('userinfo_res',res)
              var profile = res.userInfo
              wx.login({
                //获取code
                success: function (result) {
                    console.log('wxlogin',result)
                    console.log('profile',profile)
                    var code = result.code; //返回code
                    var login = this
                    console.log(code);
                    
                    wx.request({
                    url: api.userlogin,
                    data: {code:code,
                        nickname:profile.nickName,
                        avatar:profile.avatarUrl},
                    method: "POST",
                    success: (result) => {
                        console.log('wxlogres',result)
                        var phomsg ={token:result.data.data.token,userID:result.data.data.userid}
                        console.log("phomsg",phomsg)
                        app.initUserInfo(phomsg, res.userInfo,false);
                        that.setData({
                        userInfo: res.userInfo,
                        hasUserInfo: true
                        })
                        app.globalData.islogin=true
                        // wx.setStorageSync('user_info', that.data.userInfo);
                        that.setData({
                            // info:wx.getStorageSync('user_info'),
                            info:wx.getStorageSync('userInfo')
                        })
                    },
                    fail: (res) => {
                        console.log("fail",res)
                    },
                    complete: (res) => {},
                    })
                }
            })
    
            
          }
          
        })
      },
    //   getUserInfo(e) {
    //     this.setData({
    //       userInfo: e.detail.userInfo,
    //       hasUserInfo: true
    //     })
    //   },
      pswdlogin(e){
          //账号密码登录
          wx.navigateTo({
            url: '/pages/login/login',
          })
      },
    //   getdetail(e) {
    //       //根据code获取openid等信息
    //     wx.login({
    //         //获取code
    //         success: function (res) {
    //             console.log('wxlogin',res)
    //         var code = res.code; //返回code
    //         console.log(code);

    //         }
    //     })
    //     wx.getUserInfo({
    //                 withCredentials: false,
    //                 success: (result) => {
    //                     console.log("userrest",result)
    //                 },
    //                 fail: (res) => {},
    //                 complete: (res) => {},
    //             })

    //   },
      loginout:function(){
          var that = this
          wx.showModal({
            content: '退出登录？',
            showCancel: true,
            title: '提示',
            success: (result) => {
                if (result.confirm) {
                    app.logoutUserInfo();
                    that.setData({userInfo:null,info:null});
                    console.log('用户点击确定',app.globalData.userInfo,'info',that.data.info,'islog',app.globalData.islogin)
                  } else if (result.cancel) {
                    console.log('用户点击取消')
                  }
            },
            fail: (res) => {},
            complete: (res) => {},
          })
      },
      
    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {
    },
    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
        const info=wx.getStorageSync("userInfo");
        this.setData({info});
        if(this.data.info.token){
        wx.request({
          url: api.berelatednum,
          header:{
            Authorization:this.data.info.token?this.data.info.token: null
          },
          method: "GET",
          success: (result) => {
              this.setData({
                  commuinum:{"粉丝数":result.data[0].cared,"收藏数":result.data[0].collected,"点赞数":result.data[0].favored}
              })
              console.log("getrelatednum",result)
          },
          fail: (res) => {},
          complete: (res) => {},
        })}
    },
    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {
    },
    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {
    },
    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {
        if(this.data.pagestatus==0){
            this.loadpulldata(api.myrecord)
        }else if(this.data.pagestatus==1){
            this.loaddata(api.myfavor)
        }else if(this.data.pagestatus==2){
            this.loaddata(api.mycollect)
        }
        // wx.request({
        //     url:api.myrecord,
        //     data: {max_id : this.data.maxID},
        //     dataType: 'json',
        //     method: 'GET',
        //     responseType:'text',
        //     header:{
        //         Authorization: this.data.info?this.data.info.token: null
        //       },
        //     success: (result) => {
        //       if(!result.data.length){
        //         wx.showToast({
        //           title: 'No more!',
        //           icon:'loading',
        //         })
        //         wx.stopPullDownRefresh()
        //         return
        //       }
        //       console.log(result);
        //       var dataList = result.data.reverse();
        //       var cls = []
        //       var cls1 = []
        //       for (var i=0;i<dataList.length;i++){
        //         if(i%2==0){
        //           cls.push(dataList[i])
        //         }else{
        //           cls1.push(dataList[i])
        //         }
        //       }
        //       console.log('cls1',cls1,'cls',cls)
        //       this.setData({
        //         classlist:cls.concat(this.data.classlist),
        //         classlist1:cls1.concat(this.data.classlist1),
        //         maxID:dataList[0].videoID,
                
        //       })
        //     },
        //     fail: (res) => {
        //         wx.showToast({
        //           title: '请先登录',
                  
        //         })
        //     },
        //     complete: (res) => {},
        //   })
    },
    /**
     * 页面上拉触底事件的处理函数
     */
    delete:function(){

    },
    onReachBottom: function () {
        if(this.data.pagestatus==0){
            this.loadbottomdata(api.myrecord)
        }else if(this.data.pagestatus==1){
            // this.loadbottomdata(api.myfavor)
        }else if(this.data.pagestatus==2){
            // this.loadbottomdata(api.mycollect)
        }
        // wx.request({
        //     url: api.myrecord,
        //     data: {min_id : this.data.minID},
        //     header:{
        //         Authorization:this.data.info?this.data.info.token: null
        //       },
        //     dataType: 'json',
        //     method: 'GET',
        //     responseType:'text',
        //     success: (result) => {
        //       if(!result.data.length){
        //         wx.showToast({
        //           title: 'No more!',
        //           icon:'loading',
        //         })
        //         return
        //       }
        //       console.log(result);
        //       var cls = []
        //       var cls1 = []
        //       for (var i=0;i<result.data.length;i++){
        //         if(result.data[i].videoID%2==0){
        //           // console.log(result.data[i].videoID)
        //           cls.push(result.data[i])
        //         }else{
        //           // console.log(result.data[i].videoID)
        //           cls1.push(result.data[i])
        //         }
        //       }
        //       console.log('cls1',cls1,'cls',cls)
        //       this.setData({
        //         classlist:this.data.classlist.concat(cls),
        //         classlist1:this.data.classlist1.concat(cls1),
        //         minID:result.data[result.data.length-1].videoID
        //       })
        //     },
        //     fail: (res) => {
        //         wx.showToast({
        //           title: '请先登录',
        //         })
        //     },
        //     complete: (res) => {},
        //   })
    },
    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {
    }
})