// pages/scan/scan.js

// scan.js
// 移动动画
let animation = wx.createAnimation({});
// 提示音
let innerAudioContext = wx.createInnerAudioContext()
innerAudioContext.src = '/images/beep.mp3'
Page({

    /**
     * 页面的初始数据
     */
    data: {

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
    this.donghua()
    },
    donghua(){
        var that = this;
        // 控制向上还是向下移动
        let m = true
        
        setInterval(function () {
          if (m) {
            animation.translateY(650).step({ duration: 3500 })
            m = !m;
          } else {
            animation.translateY(-10).step({ duration: 3500 })
            m = !m;
          }
    
          that.setData({
            animation: animation.export()
          })
        }.bind(this), 3000)
      },
      scancode(e){
        // 提示音
        innerAudioContext.play()
        
        // 校验扫描结果，并处理
        let res = e.detail.result
        console.log(res)
        if(res){
          wx.navigateTo({
            url: '/pages/video/video?videoID=12',

            success: (result) => {},
            fail: (res) => {},
            complete: (res) => {},
          })
        }
        
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