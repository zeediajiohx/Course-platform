var api = require('../../config/api')
var app = getApp();
Page({
    data: {
      inputPassword: false,
      account: '',
      password: '',
    //   chkcode:'',
      isLogining: false,
      isaccont:false,
      ispwd:false,
    //   ischkcode:false,
    //   showckcode:false
    },
    onLoad: function() {
    //   var that = this;
    //   if (!wx.getStorageSync("openId")) {
    //     wx.cloud.callFunction({
    //       name: 'getOpenid',
    //       complete: res => {
    //         console.log('云函数获取到的openid: ', res.result.openId)
    //         wx.setStorageSync('openId', res.result.openId);
    //       }
    //     })
    //   }
    //   let account = wx.getStorageSync("account")
    //   let password = wx.getStorageSync("password")
    //   if(account&&password){
    //     that.setData({
    //       account:account,
    //       password:password
    //     })
    //   }
  
  
    },
    pwdFocus() {
      this.setData({
        inputPassword: true
      })
    },
    pwdBlur() {
      this.setData({
        inputPassword: false
      })
    },
    bindAccountInput(e) {
      if(e.detail.value){
        this.setData({
          isaccont:true
        })
      }
      this.setData({
        account: e.detail.value
      })
    //   console.log(this.data.isaccont)

    },
    bindPasswordInput(e) {
      if(e.detail.value){
        this.setData({
          ispwd:true
        })
      }
      this.setData({
        password: e.detail.value
      })
      console.log(this.data.ispwd)
    },
    
    bindchkcodeInput(e) {
      if(e.detail.value){
        this.setData({
          ischkcode:true
        })
      }
        this.setData({
          chkcode: e.detail.value
        })
        
        
      },
    bindIdentity(e) {
        
      var that = this
      if(this.data.isaccont&&this.data.ispwd){  //&&this.data.ischkcode
      that.setData({
        isLogining: true
      })
      if (!that.data.account ) {
        that.setData({
          isLogining: false
        })
        wx.showToast({
          title: '账号格式不对',
          icon: 'loading'
        })
        return
      } else 
       if (!that.data.password) {
        that.setData({
          isLogining: false
        })
        wx.showToast({
          title: '请输入密码',
          icon: 'loading'
        })
        return
      }
    //   else if (!that.data.chkcode) {
    //     that.setData({
    //       isLogining: false
    //     })
    //     wx.showToast({
    //       title: '请输入验证码',
    //       icon: 'loading'
    //     })
    //     return
    //   }
      console.log('xxx',this.data.account,this.data.password)
      wx.getUserProfile({
        desc: '授权使用您的昵称和头像',
        success: (result) => {
            wx.request({
                url:api.managerlogin,
                data: {
                  userID: that.data.account,
                  password: that.data.password,
                  nickname: result.userInfo.nickName,
                  avatar: result.userInfo.avatarUrl,
                  //code:that.data.chkcode,
                  // openId: wx.getStorageSync("openId")
                },
                method: 'POST',
                dataType:'json',
                header: {
                }, // 设置请求的 header
                success: function(res) {
                  console.log('maglogres', res)
                  if(res.data.status==false){
                    wx.showToast({
                      title: '密码或账号错误',
                      icon: 'loading'
                    })
                   
                  }
                  else if (res.data.status == true) {
                    app.globalData.islogin = true
                    // wx.setStorageSync('account', that.data.account)
                    // wx.setStorageSync('password', that.data.password)
                    app.initUserInfo(res.data.data, result.userInfo,true);
                    app.globalData.ismanager = true
                    wx.navigateBack();
        
                  } else {
                    wx.showModal({
                      title: '温馨提示',
                      content: '参数错误，请联系工作人员',
                      cancelText: '返回',
                      confirmText: '去联系',
                      confirmColor: '#7cba23',
                      success(res) {
                        if (res.confirm) {
                            wx.navigateTo({
                              url: '../service/me',
                              success: (result) => {},
                              fail: (res) => {},
                              complete: (res) => {},
                            })
                        } else if (res.cancel) {
                        }
                      }
                    })
                  } 
                },
                fail: function() {
                  console.log('fff')
                  wx.showToast({
                    title: '请检查网络',
                    icon: 'loading',
                    mask: true,
                    success: (res) => {},
                    fail: (res) => {},
                    complete: (res) => {},
                  })

                  // fail
                },
                complete: function() {
                //   console.log('cccc')
                //   // complete
                //   that.setData({
                //     isLogining: false
                //   })
                }
              })
        },
        fail: (res) => {
            var rand=Math.floor(Math.random()*(1000-100)+100)
            var nickname = 'professor-'+rand.toString()
            var avatar = 'https://s2.loli.net/2022/04/24/jrbGBPtaelQvVE9.png'
            wx.request({
                // url: 'http://authserver.cumt.edu.cn/authserver/login?service=http%3A%2F%2Fportal.cumt.edu.cn%2Fcasservice',
                url: api.managerlogin,
                data: {
                  userID: that.data.account,
                  password: that.data.password,
                  nickname: nickname,
                  avatar: avatar
                  //code:that.data.chkcode,
                  // openId: wx.getStorageSync("openId")
                },
                method: 'POST',
                dataType:'json',
                header: {
                }, // 设置请求的 header
                success: function(res) {
                  console.log('maglogres', res)
                  if(res.data.status==false){
                    wx.showToast({
                      title: '密码或账号错误',
                      icon: 'loading'
                    })
                  } else if (res.data.status == true) {
                      var frofile = {nickName:nickname,avatarUrl:avatar}
                    app.globalData.islogin = true
                    app.initUserInfo(res.data.data,frofile ,true);
                    wx.navigateBack();
                  } else {
                    wx.showModal({
                      title: '温馨提示',
                      content: '参数错误，请联系工作人员',
                      cancelText: '返回',
                      confirmText: '去联系',
                      confirmColor: '#7cba23',
                      success(res) {
                        if (res.confirm) {
                            wx.navigateTo({
                              url: '../service/me',
                              success: (result) => {},
                              fail: (res) => {},
                              complete: (res) => {},
                            })
                        //   wx.request({
                        //     url: 'http://127.0.0.1:8000/user/register/',
                        //     data: {
                        //       UserID: that.data.account,
                        //       password: that.data.password,
                        //       openId: wx.getStorageSync("openId")
                        //     },
                        //     method: 'POST',
                        //     header: {
                        //       'Content-Type': 'application/json'
                        //     }, // 设置请求的 header
                        //     success: function (res) {
                        //       if (res.data.code == 700) {
                        //         wx.setStorageSync('account', that.data.account)
                        //         wx.setStorageSync('password', that.data.password)
          
                        //         wx.switchTab({
                        //           url: '../score/score',
                        //         })
                        //       }
                        //     }
                        //   })
                        } else if (res.cancel) {
                        }
                      }
                    })
                    // 要先注册
                  } 
                //   else if(res.data.code==602){
                //     wx.showToast({
                //       title: '密码错误',
                //       icon: 'loading'
                //     })
                //   }
                //   else{
                //       console.log('eeeee',res),
                //     wx.showToast({
                //       title: '微信账号错误',
                //       icon: 'loading'
                //     })
                //   }
                },
                fail: function() {
                  console.log('fff')
                  wx.showToast({
                    title: '请检查网络',
                    icon: 'loading',
                    mask: true,
                    success: (res) => {},
                    fail: (res) => {},
                    complete: (res) => {},
                  })

                  // fail
                },
                complete: function() {
                  console.log('cccc')
                  // complete
                  that.setData({
                    isLogining: false
                  })
                }
              })
        },
        complete: (res) => {},
      })
  
      
    }
    //else if(this.data.isaccont&&this.data.ispwd){
    //   wx.request({
    //     url: ' http://127.0.0.1:8000/login/pic/code/',
    //     data: { UserID: this.data.phone },
    //   method: 'GET',
    //   dataType: 'json',
    //     // responseType: responseType,
    //     timeout: 0,
    //     success: (result) => {},
    //     fail: (res) => {},
    //     complete: (res) => {},
    //   })
    //   this.setData({
    //     showckcode:true
    //   })
    //   console.log('show',this.data.showckcode)
    //}
    else{
      wx.showToast({
        title: '请填写完整！',
        icon:'loading'
      })
    }
  
    },
  
    reset:function(e){
      console.log(e)
    //   wx.navigateTo({
    //     url: '/pages/tellogin/login',
    //   })
      wx.showToast({
        title: '尚未开放该功能',
        icon: 'loading'
      })
    },
  
    wxlogin:function(e){
        wx.switchTab({
          url: '/pages/wxlogin/wxlogin',
        })

    },
    answer:function(e){
      wx.navigateTo({
        url: '../about/about',
      })
    },
  
    onShareAppMessage: function () {
      var name = wx.getStorageSync("name")
      if(name){
        return {
          title: '扫码搜题',
          desc: name+'扫码搜题!',
        }
      }else{
        return {
          title: '扫码搜题',
          desc: '扫码搜题!',
        }
      }
  
    },
  
    onShow: function(){
      
    }
  
  })