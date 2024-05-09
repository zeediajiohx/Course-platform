// pages/entry/entry.js
var URL = require('../../config/api.js')
Page({

    /**
     * 页面的初始数据
     */
    data: {
        firstid:0,
      minID : 0,
      maxID : 0,
      classlist:[],
      usecomment:false,
    //   classlist1:[],
      currentselect:-1,
      courses:['全部','数学','英语','政治','计算机','物理','化学','材料','土木','金融','管理','建筑','环境','人文','体育','其他'],
      videos:[{
        pictures:"../../icons/cls1.png",
        titles:"当代女大学生1",
        name:"老八1",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/cls3.png",
        titles:"太原动物园的动物有毒吧",
        name:"老八2",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/cls4.png",
        titles:"我妈让我把这个列入年夜饭新系列！",
        name:"老八3",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/cls5.png",
        titles:"当代女大学生2",
        name:"老八4",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/custom-empty-image.png",
        titles:"隐形门已无力吐槽",
        name:"老八5",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/enterpic.png",
        titles:"llll",
        name:"老八6",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/peng.jpg",
        titles:"我妈让我把这个列入年夜饭新系列！2",
        name:"老八7",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/niu.jpg",
        titles:"当代女大学生3",
        name:"老八8",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/peng.jpg",
        titles:"隐形门已无力吐槽4",
        name:"老八9",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/pig.jpg",
        titles:"太原动物园的动物有毒吧3",
        name:"老八10",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/cls1.png",
        titles:"ccfgfs",
        name:"老八11",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/enterpic.png",
        titles:"llll",
        name:"老八6",
        sculp:"../../icons/cls5.png"
      }],
      video1:[{
        pictures:"../../icons/cls3.png",
        titles:"太原动物园的动物有毒吧",
        name:"老八2",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/cls4.png",
        titles:"我妈让我把这个列入年夜饭新系列！",
        name:"老八3",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/cls5.png",
        titles:"当代女大学生2",
        name:"老八4",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/pig.jpg",
        titles:"隐形门已无力吐槽",
        name:"老八5",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/cls1.png",
        titles:"当代女大学生1",
        name:"老八1",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/enterpic.png",
        titles:"我妈让我把这个列入年夜饭新系列！2",
        name:"老八7",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/niu.jpg",
        titles:"当代女大学生3",
        name:"老八8",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/peng.jpg",
        titles:"隐形门已无力吐槽4",
        name:"老八9",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/pig.jpg",
        titles:"太原动物园的动物有毒吧3",
        name:"老八10",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/female.png",
        titles:"ccfgfs",
        name:"老八11",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/enterpic.png",
        titles:"llll",
        name:"老八6",
        sculp:"../../icons/cls5.png"
      },{
        pictures:"../../icons/pig.jpg",
        titles:"太原动物园的动物有毒吧3",
        name:"老八10",
        sculp:"../../icons/cls5.png"
      }],
      info:wx.getStorageSync('userInfo'),
      statusheight:0,
      usenews:false,
    },
    selectclass:function(index){
        // if(this.data.currentselect!=-1){
        //     var selclasslist=[]
        //     for (var item=0 ;item<this.data.classlist.length;item++){
        //         if(this.data.classlist[item].topic.id==index+1){
        //             selclasslist.push(this.data.classlist[item])
        //         }
        //         console.log("selectclslis",index,this.data.classlist[item].topic.id)
        //     }
        //     this.setData({
        //         // classlist1:selclasslist1,
        //         classlist:selclasslist
        //     })
        // }
        wx.request({
          url: this.data.usecomment? URL.careselect:URL.selecttopic,
          data: {
            topic : index+1,
          },
          header:{
            Authorization:this.data.info.token?this.data.info.token: null
          },
          dataType: 'json',
          method: 'GET',
          responseType: 'text',
          success: (result) => {
              console.log("seleres",result)
              if(result.data.length){
                  this.setData({
                      classlist:result.data,
                      minID:result.data[result.data.length-1].videoID,
                      maxID:result.data[0].videoID
                  })
              }
          },
          fail: (res) => {
              wx.showToast({
                title: '请求失败，请检查网络！'
              })
          },
          complete: (res) => {},
        })

       
       
        // var selclasslist1=[]
        // for (var item=0 ;item<this.data.classlist1.length;item++){
        //     if(this.data.classlist1[item].topic.id==index){
        //         selclasslist1.push(this.data.classlist1[item])
        //     }
        // }
        
    },
    choosekind:function(e){
        var index=e.currentTarget.dataset.index;
        this.setData({
        currentselect:index,
        })
        
        this.selectclass(index)

    },
    allclass:function(){
        this.setData({
            currentselect:-1
        })
        this.getclass()
    },
    /**
     * 生命周期函数--监听页面加载
     */
    getclasspation:function(){
        wx.request({
            url: this.data.usecomment? URL.careall:URL.indexURL,
            dataType: 'json',
            method: 'GET',
            responseType: 'text',
            header:{
                Authorization:this.data.info.token?this.data.info.token: null
              },
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
            //   console.log('cls1',cls1,'cls',cls)
              this.setData({
                classlist:cls,
                classlist1:cls1,
                minID:result.data[result.data.length-1].videoID,
                maxID:result.data[0].videoID
              })
            },
            fail: (res) => {
              console.log('fail',URL.indexURL)
            },
            complete: (res) => {},
          })
    },
    getclass:function(){
        wx.request({
            url: this.data.usecomment? URL.careall:URL.indexURL,
            dataType: 'json',
            method: 'GET',
            responseType: 'text',
            header:{
                Authorization:this.data.info.token?this.data.info.token: null
              },
            success: (result) => {
            //   console.log(result)
              //最大和最小ID
              if(result.statusCode==200){
                  if(result.data.length){
                this.setData({
                classlist:result.data,
                // classlist1:cls1,
                minID:result.data[result.data.length-1].videoID,
                maxID:result.data[0].videoID
              })
              console.log("clsls",this.data.classlist)
              }}
              this.setData({
                  firstid:result.data[0].videoID
              })
            },
            fail: (res) => {
              console.log('fail',URL.indexURL)
            },
            complete: (res) => {},
          })
    },
    onLoad: function () {
        // 去获取顶栏分类
        wx.getSystemInfo({
            success: (result) => {
                console.log(result)
                this.setData({
                    statusheight:result.statusBarHeight,
                })
            },
          })
        wx.request({
            url: URL.topic,
            method: 'GET',
            dataType: 'json',
            responseType: 'text',
            success: (res)=> {
              
              this.setData({ courses: res.data})
            }
          })
      //去数据库获取最新的10条
      this.getclass()
      
    },
    
    /**
     * 搜索函数
     */
    search: function (e) {
        wx.scanCode({
            success (res) {
                
              console.log("scannn",res)
            //   pages/video/video?scene=videoID=36
              if(res.path.split('=')[0]=='pages/video/video?scene'||res.rawData=='bDNzP2wydy4kQH4kaEMnL353OUNFdz0zNA=='){
                  var urlpath 
                  if(res.path.split('=')[1][7]=='%'){
                      urlpath = res.path.split('=')[1].slice(10)
                  }else if(res.path.split('=')[2]){
                    urlpath=res.path.split('=')[2]
                  }
              
              wx.navigateTo({
                url: '/pages/video/video?videoID=' + urlpath,
              })
            }
            else{
                wx.showToast({
                  title: '非本平台课程!',
                })
                return
            }
            }
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
        this.setData({
            info:wx.getStorageSync('userInfo')
        })
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
    tocomment:function(){
        if(!this.data.info.token){
            wx.switchTab({
                url: '/pages/wxlogin/wxlogin',
              })
            return}
        this.setData({
            usecomment:true,
            classlist:[]
            // classlist:this.data.classlist.reverse()
        })
        this.onLoad()
    },
    
    cancelcomment:function(){
        this.setData({
            usecomment:false,
            usenews:false,
            classlist:[]
        })
        this.onLoad()
    },
    getneewest:function(){
        this.setData({
            usenews:true,
            usecomment:true,
            classlist:this.data.classlist.reverse()
        })
        // this.onLoad()
    },
    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    
    onPullDownRefresh: function () {
        if(this.data.currentselect==-1){
      wx.request({
        url:this.data.usecomment? URL.careall:URL.indexURL,
        data: {max_id : this.data.maxID},
        dataType: 'json',
        method: 'GET',
        responseType:'text',
        header:{
            Authorization:this.data.info.token?this.data.info.token: null
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
          var dataList = result.data.reverse();
        //   var cls = []
        //   var cls1 = []
        //   for (var i=0;i<dataList.length;i++){
        //     if(i%2==0){
        //       cls.push(dataList[i])
        //     }else{
        //       cls1.push(dataList[i])
        //     }
        //   }
        //   console.log('cls1',cls1,'cls',cls)
          this.setData({
            classlist:dataList.concat(this.data.classlist) ,
            // classlist1:cls1.concat(this.data.classlist1),
            maxID:dataList[0].videoID,
            
          })
          console.log("clsls",this.data.classlist)

        //   if(this.data.currentselect!=-1){
        //       this.selectclass(this.data.currentselect)
        //   }
        },
        fail: (res) => {},
        complete: (res) => {},
      })}
      else{
        wx.request({
            url:this.data.usecomment? URL.careselect:URL.selecttopic,
            data: {max_id : this.data.maxID,
            topic:this.data.currentselect+1},
            dataType: 'json',
            method: 'GET',
            responseType:'text',
            header:{
                Authorization:this.data.info.token?this.data.info.token: null
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
              var dataList = result.data.reverse();
              this.setData({
                classlist:dataList.concat(this.data.classlist) ,
                maxID:dataList[0].videoID,
              })
              console.log("clsls",this.data.classlist)
            },
            fail: (res) => {},
            complete: (res) => {},
          })

      }

    },
    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {
        if(this.data.currentselect==-1){
            wx.request({
                url: this.data.usecomment? URL.careall:URL.indexURL,
                data: {min_id : this.data.minID},
                dataType: 'json',
                method: 'GET',
                responseType:'text',
                header:{
                    Authorization:this.data.info.token?this.data.info.token: null
                  },
                success: (result) => {
                    if(result.statusCode==200){
                  if(!result.data.length){
                    wx.showToast({
                      title: 'No more!',
                      icon:'loading',
                    })
                    return
                  }
                //   var cls = []
                //   var cls1 = []
                //   for (var i=0;i<result.data.length;i++){
                //     if(result.data[i].videoID%2==0){
                //       // console.log(result.data[i].videoID)
                //       cls.push(result.data[i])
                //     }else{
                //       // console.log(result.data[i].videoID)
                //       cls1.push(result.data[i])
                //     }
                //   }
                //   console.log('cls1',cls1,'cls',cls)
                  this.setData({
                    classlist:this.data.classlist.concat(result.data),
                    // classlist1:this.data.classlist1.concat(cls1),
                    minID:result.data[result.data.length-1].videoID
                  })
                //   if(this.data.currentselect!=-1){
                //     this.selectclass(this.data.currentselect)
                // }
                    }
                    else{
                        wx.showToast({
                            title: '获取失败，请检查网络',
                            
                          })
                    }
                },
                fail: (res) => {
                    
                },
                complete: (res) => {},
              })
        }
        else{
            wx.request({
                url: this.data.usecomment? URL.careselect:URL.selecttopic,
                data: {min_id : this.data.minID,
                topic:this.data.currentselect+1},
                dataType: 'json',
                method: 'GET',
                responseType:'text',
                header:{
                    Authorization:this.data.info.token?this.data.info.token: null
                  },
                success: (result) => {
                    if(result.statusCode==200){
                  if(!result.data.length){
                    wx.showToast({
                      title: 'No more!',
                      icon:'loading',
                    })
                    return
                  }
                  this.setData({
                    classlist:this.data.classlist.concat(result.data),
                    minID:result.data[result.data.length-1].videoID
                  })
                    }
                    else{
                        wx.showToast({
                            title: '获取失败，请检查网络',
                            
                          })
                    }
                },
                fail: (res) => {
                    
                },
                complete: (res) => {},
              })
        }
      
    },
    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})