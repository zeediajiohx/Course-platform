// pages/release/release.js
var COS = require('../../utils/cos-wx-sdk-v5')
var api = require('../../config/api')
var app = getApp();
var cos;
Page({
    

    /**
     * 页面的初始数据
     */
    data: {
        imageList: [],
        videoList:[],
    content: "",
    title: "",
    address: "anywhere",
    topicId: null,
    topicTitle: "选择合适的话题",
    cantpbls:true,
    info:wx.getStorageSync('userInfo')


    },
    resetData: function() {
        this.setData({
          imageList: [],
          videoList: [],
          content: "",
          address: " anywhere",
          topicId: null,
          topicTitle: "选择合适的话题",
        });
      },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        // console.log("mana?",!app.globalData.ismanager)
        // this.setData({
        //     cantpbls:!app.globalData.ismanager
        // })
        console.log('rlsapp',app.globalData.islogin,app.globalData.userInfo)
        if (wx.getStorageSync('userInfo').token==false) {
            wx.navigateTo({
              url: '../login/login',
            })
            
        }

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
            // cantpbls:!app.globalData.ismanager
            info:wx.getStorageSync('userInfo'),
            cantpbls:!wx.getStorageSync("userInfo").ismanager
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

    uploadImage: function() {
        // 选择图片并上传
        wx.chooseImage({
          count: 1,
          sizeType: ['original', 'compressed'],
          sourceType: ['album', 'camera'],
          success: res => {
            var oldLength = parseInt(this.data.imageList.length);
            // 最多上传9张
            
            let totalCount = res.tempFiles.length + this.data.imageList.length;
            if (totalCount > 1) {
              wx.showToast({
                title: '图片最多选择1张',
                icon: 'none'
              });
              return
            };
            console.log(this.data.imageList.concat(res.tempFiles));
            // 本地图片在页面预览
            this.setData({
              imageList: this.data.imageList.concat(res.tempFiles)
            });
    
            // 获取腾讯对象存储上传文件临时秘钥，并设置到全局变量中。
            cos = new COS({
              getAuthorization: function(options, callback) {
                wx.request({
                  url: api.Credential,
                  data: {},
                  success: function(result) {
                    var data = result.data;
                    var credentials = data.credentials;
                    callback({
                      TmpSecretId: credentials.tmpSecretId,
                      TmpSecretKey: credentials.tmpSecretKey,
                      XCosSecurityToken: credentials.sessionToken,
                      ExpiredTime: data.expiredTime,
                    });
                  }
                });
              }
            });
    
            // 上传新挑选的图片
            for (var index in res.tempFiles) {
    
              let imageFilePath = res.tempFiles[index].path;
    
              var filePathSplit = imageFilePath.split('.');
              var ext = filePathSplit[filePathSplit.length - 1];
              // 创建随机字符串
              let randowString = Math.random().toString(36).slice(-8) + String(new Date().getTime());
              var fileKey = randowString + "." + ext;
              
              var targetIndex = parseInt(oldLength) + parseInt(index);
              this.setData({
                ["imageList[" + targetIndex + "].key"]: fileKey
              });
              var that = this;

              


              // 上传文件（通过闭包做一个上传文件的操作）
              (function(idx){
                cos.postObject({
                  Bucket: "videotest1-1301605345",
                  Region: "ap-nanjing",
                  Key: fileKey,
                  FilePath: imageFilePath,
                  onProgress: (info) => {
                    that.setData({
                      ["imageList[" + idx + "].percent"]: info.percent * 100
                    })
                  }
                }, (err, data) => {
                    console.log("data",data)
                  // 上传成功或失败
                  if (err) {
                    wx.showToast({
                      title: '上传失败',
                      icon: 'none'
                    });
                    that.setData({
                      ["imageList[" + idx + "].error"]: true,
                      ["imageList[" + idx + "].percent"]: 100
                    })
                  } else {
                    console.log("data22", data.headers.location)
                    that.setData({
                      ["imageList[" + idx + "].cos_path"]: data.headers.location
                    });
                    console.log("imgls",that.data.imageList[idx])
                  }
                });
              })(targetIndex)
              
            }
          }
        })
      },
    uploadvideo: function() {
        // 选择图片并上传
        wx.chooseVideo({
        //   count: 1,
        //   mediaType:'video',
        //   sizeType: ['original', 'compressed'],
          sourceType: ['album', 'camera'],

          success: res => {
            var oldLength = parseInt(this.data.videoList.length);
            // 最多上传1个
            console.log("videorest",res,oldLength)
            let totalCount = 1 + this.data.videoList.length;
            if (totalCount > 1) {
              wx.showToast({
                title: '视频最多选择1个',
                icon: 'none'
              });
              return
            };
            console.log('ttt',this.data.videoList.concat(res));
    
            // 本地图片在页面预览
            this.setData({
              videoList: this.data.videoList.concat(res)
            });
    
            // 获取腾讯对象存储上传文件临时秘钥，并设置到全局变量中。
            cos = new COS({
              getAuthorization: function(options, callback) {
                wx.request({
                  url: api.Credential,
                  data: {},
                  success: function(result) {
                    var data = result.data;
                    var credentials = data.credentials;
                    callback({
                      TmpSecretId: credentials.tmpSecretId,
                      TmpSecretKey: credentials.tmpSecretKey,
                      XCosSecurityToken: credentials.sessionToken,
                      ExpiredTime: data.expiredTime,
                    });
                  }
                });
              }
            });
    
            // 上传新挑选的图片（原图片无需再上传）
            for (var index in [res]) {
    
              let videoFilePath = res.tempFilePath;
    
              var filePathSplit = videoFilePath.split('.');
              var ext = filePathSplit[filePathSplit.length - 1];
              // 创建随机字符串
              let randowString = Math.random().toString(36).slice(-8) + String(new Date().getTime());
              var fileKey = randowString + "." + ext;
              
              var targetIndex = parseInt(oldLength) + parseInt(index);
              this.setData({
                ["videoList[" + targetIndex + "].key"]: fileKey
              });
              var that = this;

              


              // 上传文件（通过闭包做一个上传文件的操作）
              (function(idx){
                cos.postObject({
                  Bucket: "videotest1-1301605345",
                  Region: "ap-nanjing",
                  Key: fileKey,
                  FilePath: videoFilePath,
                  onProgress: (info) => {
                    that.setData({
                      ["videoList[" + idx + "].percent"]: info.percent * 100
                    })
                  }
                }, (err, data) => {
                  // 上传成功或失败
                  if (err) {
                    wx.showToast({
                      title: '上传失败',
                      icon: 'none'
                    });
                    that.setData({
                      ["videoList[" + idx + "].error"]: true,
                      ["videoList[" + idx + "].percent"]: 100
                    })
                  } else {
                      console.log(data)
                    that.setData({
                      ["videoList[" + idx + "].cos_path"]: data.headers.location
                    });
                    console.log("idxvideo",that.data.videoList[idx])
                  }
                });
              })(targetIndex)
              
            }
          }
        })
      },
    removeImage: function(event) {
        // 判断是否正在上传，如果正在上传就终止，否则就删除；
        // 删除图片，终止 & 删除
        var index = event.currentTarget.dataset['index'];
        var item = event.currentTarget.dataset['item'];
        if (item.percent == 100) {
          cos.deleteObject({
            Bucket: "videotest1-1301605345",
            Region: "ap-nanjing",
            Key: item.key
          }, (err, data) => {
            if (err) {
              wx.showToast({
                title: '删除失败',
                icon: 'none'
              });
            } else {
              var imageList = this.data.imageList;
              imageList.splice(index, 1);
              this.setData({
                imageList: imageList
              });
            }
          });
        }
    
    
      },
    removeVideo: function(event) {
        // 判断是否正在上传，如果正在上传就终止，否则就删除；
        // 删除图片，终止 & 删除
        var index = event.currentTarget.dataset['index'];
        var item = event.currentTarget.dataset['item'];
        if (item.percent == 100) {
          cos.deleteObject({
            Bucket: "videotest1-1301605345",
            Region: "ap-nanjing",
            Key: item.key
          }, (err, data) => {
            if (err) {
              wx.showToast({
                title: '删除失败',
                icon: 'none'
              });
            } else {
              var videoList = this.data.videoList;
              videoList.splice(index, 1);
              this.setData({
                videoList: videoList
              });
            }
          });
        }
    
    
      },
    getLocation: function() {
        // wx.chooseLocation({
        //   success: res => {
        //     this.setData({
        //       address: res.address
        //     })
        //   }
        // });
      },
    updateTopic: function(item) {
        this.setData({
          topicId: item.id,
          topicTitle: item.title
        })
      },
    bindContentInput: function(e) {
        this.setData({
          content: e.detail.value
        });
      },
      bindtitleInput: function(e) {
        this.setData({
          title: e.detail.value
        });
      },
    publishNews: function() {
    if(!this.data.cantpbls){
        //发布至少需要一张图片
        if (this.data.imageList.length < 1) {
          wx.showToast({
            title: '请选择一张封面',
            icon: 'none'
          });
          return
        }else if (this.data.videoList.length < 1) {
            wx.showToast({
              title: '请选择一个视频',
              icon: 'none'
            });
            return
          }
        // 发布内容不能为空
        if (this.data.content.length < 1) {
          wx.showToast({
            title: '请输入内容和标题',
            icon: 'none'
          });
          return
        }
    
        wx.showLoading({
          title: '发布中...',
          
        })
        var vidlst = [{
            key:this.data.videoList[0].key,
            cos_path :this.data.videoList[0].cos_path
        }]
        wx.request({
          url: api.test,
          data: {

            icon: this.data.imageList[0].cos_path,
            // video: this.data.videoList[0].cos_path,
            //title:this.data.title,
            content: this.data.content,
            topic: this.data.topicId,
            address: this.data.address,
            // imageList: this.data.imageList,
            videoList: vidlst,
            // academy:"cumputerscience",
            // subject:"bigdata",
            // section:"database",
            // name:"hhhhhh",

          },
          header: {
            Authorization: this.data.info.token?this.data.info.token: null
          },
          method: 'POST',
          dataType: 'json',
          responseType: 'text',

          success: (res) => {
            if (res.statusCode == 201) {
                console.log({
                    "icon": this.data.imageList[0].cos_path,
                    "content": this.data.content,
                    "topic": this.data.topicId,
                    "address": this.data.address,
                    "videoList": vidlst,
                })
              // 发布成功，跳转到一个页面进行提示
              wx.navigateTo({
                url: '/pages/publishSuccess/publishSuccess',
              })
             
            } else {
                console.log({
                    "icon": this.data.imageList[0].cos_path,
                    "content": this.data.content,
                    "topic": this.data.topicId,
                    "address": this.data.address,
                    "videoList": vidlst,
                })
              wx.showToast({
                title: '发布失败！',
                icon: 'none'
              });
            }
    
          },
          fail: (res) => {
              console.log(res)
            wx.showToast({
              title: '发布失败,请先登录管理员账号',
              icon: 'none'
            });
          },
          complete: (res) => {
            wx.hideLoading();
          },
        })
    
      }else {
          wx.showToast({
            title: '请使用管理员账号发布！',
            icon:'none',
            success: (res) => {},
            fail: (res) => {},
            complete: (res) => {},
          })
      }
    }
})