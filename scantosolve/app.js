// app.js
App({
    globalData: {
        userInfo: null,
        islogin: false,
        hascompletuserinfo: false,
        ismanager: false,
        // appid:'wx168cffb5b9b379e0',
        // AppSecret:'5f533527928d334b9a3bfc3b5210d09d',
        // access_token:"56_APOcgDTBOl95bn2doYXRYYwLc6dX_KNsGLxA9qTlROnX9gzrAhOXCs2DPLSFW-knwOV9egNgLnIoLL0x6csBa5-4mABgvyjNaeGu7NPJeTorgeaV307ccnrm4L_rthUSW_ZIUkH0Ex9_V96JRHWiAIAMCR"
      },
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })

    var userInfo = wx.getStorageSync('userInfo');
    if (userInfo) {
        console.log("getstoryuser",userInfo)
      this.globalData.userInfo = userInfo;
        console.log('glbdtusif',this.globalData.userInfo)
    //   this.globalData.islogin = true;
    }
  },
  
  initUserInfo: function (res, localInfo,manage) {
    var info = {
      token: res.token,
      userid: res.userid,
      nickName: localInfo.nickName,
      avatarUrl: localInfo.avatarUrl,
      ismanager: manage
    }
    // 1.去公共的app.js中调用globalData，在里面赋值。(在全局变量赋值)
    this.globalData.userInfo = info;//{phone:xxx,token:xxxx}

    // 2.在本地“cookie”中赋值
    wx.setStorageSync("userInfo", info);
    this.globalData.islogin=true;

  },
  logoutUserInfo:function(){
    wx.removeStorageSync('userInfo');
    this.globalData.userInfo=null;
    this.globalData.islogin=false;
    this.globalData.ismanager=false;
  }
})
