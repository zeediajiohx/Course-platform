// pages/complinfo/complinfo.js
var api = require('../../config/api.js')

Page({

    /**
     * 页面的初始数据
     */
    data: {
        nickname:wx.getStorageSync('userInfo').nickName,
        phone:wx.getStorageSync('phone'),
        acadamy:wx.getStorageSync('acdemy'),
        major:wx.getStorageSync('major'),
        gender:"女",
        grade:"18",
        phonemessage:'',
        columns:['男','女','不愿透露'],
        currentDate: new Date().getTime(),
        maxDate: new Date().getTime(),
        showpop:false,
        info:wx.getStorageSync('userInfo'),
        complitied:true,


    },
    selectgender:function(){
        var that = this
        this.setData({
            showpop:!that.data.showpop
        })
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad(options) {

    },
    onChangename(event) {
        // event.detail 为当前输入的值
        this.setData({
            nickname:event.detail
        })
        if(this.data.nickname){
            this.setData({
                complitied:false
            })
        }
      },
      onChangephone(event) {
        // event.detail 为当前输入的值
        this.setData({
            phone:event.detail
        })
        var reg = /^(1[3|4|5|6|7|8|9])\d{9}$/;
        if (!reg.test(this.data.phone)||!this.data.phone||this.data.phone.length<11 ){
            this.setData({
                phonemessage:"手机号格式错误"
            })
        }else{
            this.setData({
                phonemessage:""
            })
        }
      },
      onChangeacademy(event) {
        // event.detail 为当前输入的值
        this.setData({
            acadamy:event.detail
        })
      },
      onChangemajor(event) {
        // event.detail 为当前输入的值
        this.setData({
            major:event.detail
        })
      },
      onchangegrade(event) {
        // event.detail 为当前输入的值
        this.setData({
            grade:event.detail
        })
      },
      onchangegender(event) {
        // event.detail 为当前输入的值
        this.setData({
            gender:event.detail
        })
      },
      submit:function(){
          if(!this.data.acadamy){
              this.setData({
                  acadamy:"学院"
              })
          }
          if(!this.data.major){
              this.setData({
                  major:"专业"
              })
          }
          if(!this.data.gender){
              this.setData({
                  gender:"不愿透露"
              })
          }
          if(!this.data.grade){
              this.setData({
                  grade:"无所谓"
              })
          }
        console.log("nm",this.data.nickname,this.data.phone,this.data.major,this.data.acadamy,this.data.gender,this.data.grade)
        if(this.data.nickname){
            wx.request({
                url: api.infoupdate,

                data: {
                    nickname:this.data.nickname,
                    academy:this.data.acadamy,
                    major:this.data.major,
                    sex:this.data.gender,
                    grade:this.data.grade
                },
                header: {
                  Authorization: this.data.info.token?this.data.info.token: null
                },
                method:"POST",
                success: (result) => {
                    console.log("inforesult",result)
                    if(result.statusCode==200){
                        console.log("strg",this.data.nickname)
                        this.setData({
                            ["info.nickName"]:this.data.nickname
                        })
                        console.log(this.data.info)
                        wx.setStorageSync('userInfo',this.data.info)
                        wx.setStorageSync('academy', this.data.acadamy)
                        wx.setStorageSync('major', this.data.major)
                        wx.setStorageSync('phone', this.data.phone)
                        wx.navigateBack({
                          delta: 1,

                        })
                        
                    }

                },
                fail: (res) => {
                    
                },
                complete: (res) => {},
              })
        }else{
            wx.showToast({
              title: '请填昵称',
            })
        }

        
      },
    onInput(event) {
        this.setData({
          currentDate: event.detail,
        });
      },
    onConfirm(event) {
        const { picker, value, index } = event.detail;
        this.setData({
            gender:value
        })
      },
    
      onCancel() {
        Toast('取消');
      },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady() {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow() {
        this.setData({
            info:wx.getStorageSync('userInfo'),
            nickname:wx.getStorageSync('userInfo').nickName,
            acadamy:wx.getStorageSync('acdemy'),
            major:wx.getStorageSync('major'),
        })
    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide() {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload() {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh() {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom() {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage() {

    }
})