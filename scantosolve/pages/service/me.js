// pages/me/me.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        phone:"",
        chkcode:"",
    },
    logID:function(e){
        console.log(e);
        this.setData({phone:e.detail.value});
    },
    logchk:function(e){
        console.log(e);
        this.setData({chkcode:e.detail.value});
    },
    messchk:function(e){
        // console.log(this.data.phone,this.data.chkcode);
        //从后端获取验证码
        if(this.data.phone.length != 11){//手机长度限制
            wx.showToast({
              title: '手机号错误',
              icon:'error',
            })
            return;
        }
        var reg = /^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$/
        if(!reg.test(this.data.phone)){
            wx.showToast({
                title: '手机号格式错误',
                icon:'error',
              })
              return;
        }
        wx.request({
          url: 'http://127.0.0.1:8000/message/',
          data: {phone:this.data.phone},
          method: 'GET',
          success: function(res) {
              console.log(res);
          },
          fail: (res) => {},
          complete: (res) => {},
        })
    },
    login:function(){
        console.log(this.data.phone,this.data.chkcode);
        //将手机号和验证码发送后端
        wx.request({
          url: 'http://127.0.0.1:8000/login/',
          data: {phone:this.data.phone, chkcode:this.data.chkcode},
          method: 'POST',
          success: function(res) {
              console.log(res);
          },
          fail: (res) => {},
          complete: (res) => {},
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