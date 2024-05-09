// pages/register/register.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        userID:'',
        password:'',
        repassword:'',
        chkcode:"",
        islogin:false,
        inputPassword:false,
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
        this.setData({
          account: e.detail.value
        })
      },
      bindPasswordInput(e) {
        this.setData({
          password: e.detail.value
        })
      },
      
      bindchkcodeInput(e) {
          this.setData({
            chkcode: e.detail.value
          })
        },
    bindrepwdInput(e){
        this.setData({
          repassword: e.detail.value
        })
      },
    bindRegiste(e){
        var app = getApp()
        var that = this
        var reg = /^(1[3|4|5|6|7|8|9])\d{9}$/;
    if(!that.data.userID||that.data.userID.length<11 ){
            wx.showToast({
                title: '账号格式不对',
                icon: 'loading'
              })
        } else if (!reg.test(that.data.userID)) {
            wx.showToast({
              title: '手机格式错误',
              icon: 'none'
            })}else if(!that.data.password){
            wx.showToast({
              title: '请输入密码！',
              icon:"loading"
            })
        }else if(that.data.password.length<6){
            wx.showToast({
              title: '密码少于6位！',
            })
        }
        else if(that.data.password!=that.data.repassword){
            wx.showToast({
              title: '两次密码不一致！',
              icon: error,
            })
        }else  if(!that.data.chkcode){
            wx.showToast({
              title: '请输入验证码！',
              icon: 'loading'
            })
            return
        }
        wx.request({
          url: 'http://127.0.0.1:8000/user/register/',
          data: {
              userID: that.data.account,
            password: that.data.password,
            code:that.data.chkcode,},
          method: 'POST',
          header: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          success: (result) => {
            if(res.Code==1){
                wx.showToast({
                  title:'账号已存在，请登录，或联系管理员找回密码！',
                  icon: 'loading'
                })
              }else if (res.Code == 1) {
                app.globalData.islogin = true
                wx.setStorageSync('account', that.data.account)
                wx.setStorageSync('password', that.data.password)
                wx.navigateTo({
                  url: '../me/me',
                })
              } 
          },
          fail: (res) => {
            console.log('fff')
            // fail
          },
          complete: (res) => {
            console.log('cccc')
            // complete
            that.setData({
              isLogining: false
            })
          },
        })
    },
    wxlogin:function(e){
        wx.switchTab({
          url: '/pages/wxlogin/wxlogin',
        })
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

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

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})