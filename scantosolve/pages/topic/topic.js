// pages/topic/topic.js
const api = require("../../config/api")
Page({

  /**
   * 页面的初始数据
   */
  data: {
    topicList:[
        // {title:'数学',count:"0"},
        // {title:'英语',count:"0"},
        // {title:'政治',count:"0"},
        // {title:'计算机',count:"0"},
        // {title:'物理',count:"0"},
        // {title:'化学',count:"0"},
        // {title:'材料',count:"0"},
        // {title:'土木',count:"0"},
        // {title:'金融',count:"0"},
        // {title:'管理',count:"0"},
        // {title:'建筑',count:"0"},
        // {title:'环境',count:"0"},
        // {title:'人文',count:"0"},
        // {title:'其他',count:"0"},
        // {title:"",count:""},
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
      wx.request({
        url: api.topic,
        method: 'GET',
        dataType: 'json',
        responseType: 'text',
        success: (res)=> {
          this.setData({ topicList:res.data})
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

  },
  choseTopic:function(event){
      var topicItem = event.currentTarget.dataset['item'];
      var pages = getCurrentPages();
      var prevPage = pages[pages.length - 2];  //上一个页面
      prevPage.updateTopic(topicItem);
      wx.navigateBack()
  }
})