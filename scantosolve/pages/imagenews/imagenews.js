// pages/video/video.js
const api = require("../../config/api")
var URL = require("../../config/api")
// var app = getApp()
var videoid
Page({

    /**
     * 页面的初始数据
     */
    data: {
        news:[],
        videopage:true,
        customStyle :'',
        danmulist:[],
        reply: {},
        codeurl: api.codeurl,
        info:wx.getStorageSync('userInfo'),
        showpage:false,
        showcomment:false,
        showcontent:false,
        scanbutton:false,
        thisindex:0,
        videolist:[
          {
              title:"shuzu",
            content:"数组",
            images:{id:80,cos_path: "https://stream7.iqilu.com/10339/article/202002/18/2fca1c77730e54c7b500573c2437003f.mp4"},
            imooo:"https://vdn3.vzuu.com/HD/03bf94a2-a031-11ec-a85a-22371603121a-v4_t10001111-wdkLGxoqDa.mp4?disable_local_cache=1&amp;",
            qrcode:"https://qr.api.cli.im/newqr/create?data=https%253A%252F%252Fstream7.iqilu.com%252F10339%252Farticle%252F202002%252F18%252F2fca1c77730e54c7b500573c2437003f.mp4&level=H&transparent=false&bgcolor=%23FFFFFF&forecolor=%23000000&blockpixel=12&marginblock=1&logourl=&logoshape=no&size=500&kid=cliim&key=8f8f55b9645038cfacaf7869eba614e6"
          },
          {
            title:"数组",
            content:"二维数组就是元素是数组的一维数组，。。。。",
            images:{id:81,cos_path: "https://www.w3schools.com/html/movie.mp4"},
            imooo:"https://vdn3.vzuu.com/HD/03bf94a2-a031-11ec-a85a-22371603121a-v4_t10001111-wdkLGxoqDa.mp4?disable_local_cache=1&amp;",
            qrcode:"https://qr.api.cli.im/newqr/create?data=https%253A%252F%252Fwww.w3schools.com%252Fhtml%252Fmovie.mp4&level=H&transparent=false&bgcolor=%23ffffff&forecolor=%23000000&blockpixel=12&marginblock=1&logourl=&logoshape=no&size=500&kid=cliim&key=e7c07b987e95076ecbbb461c3e5b8c21"
          },
          {
            content:"栈",
            images:{id:82,cos_path: "https://stream7.iqilu.com/10339/upload_transcode/202002/16/20200216050645YIMfjPq5Nw.mp4"},
            qrcode:"https://qr.api.cli.im/newqr/create?data=https%253A%252F%252Fstream7.iqilu.com%252F10339%252Fupload_transcode%252F202002%252F16%252F20200216050645YIMfjPq5Nw.mp4&level=H&transparent=false&bgcolor=%23ffffff&forecolor=%23000000&blockpixel=12&marginblock=1&logourl=&logoshape=no&size=500&kid=cliim&key=376a7527a909c32703e8d03266a1430c"
          },
          {
            content:"数组",
            images:{id:83,cos_path: "http://stream4.iqilu.com/ksd/video/2020/02/17/97e3c56e283a10546f22204963086f65.mp4"},
            qrcode:"https://qr.api.cli.im/newqr/create?data=http%253A%252F%252Fstream4.iqilu.com%252Fksd%252Fvideo%252F2020%252F02%252F17%252F97e3c56e283a10546f22204963086f65.mp4&level=H&transparent=false&bgcolor=%23ffffff&forecolor=%23000000&blockpixel=12&marginblock=1&logourl=&logoshape=no&size=500&kid=cliim&key=49547ba91af0a24318f9a67d4e85512e"
          },
          {
            content:"数组",
            images:{id:84,cos_path: "https://media.w3.org/2010/05/sintel/trailer.mp4"},
            qrcode:"https://qr.api.cli.im/newqr/create?data=https%253A%252F%252Fmedia.w3.org%252F2010%252F05%252Fsintel%252Ftrailer.mp4&level=H&transparent=false&bgcolor=%23ffffff&forecolor=%23000000&blockpixel=12&marginblock=1&logourl=&logoshape=no&size=500&kid=cliim&key=2d340584a054975dc1a92e469b9a14dc"

          },
          {
            content:"数组",
            images:{id:85,cos_path: "http://stream.iqilu.com/vod_bag_2016//2020/02/16/903BE158056C44fcA9524B118A5BF230/903BE158056C44fcA9524B118A5BF230_H264_mp4_500K.mp4"},
            qrcode:"https://qr.api.cli.im/newqr/create?data=http%253A%252F%252Fstream.iqilu.com%252Fvod_bag_2016%252F%252F2020%252F02%252F16%252F903BE158056C44fcA9524B118A5BF230%252F903BE158056C44fcA9524B118A5BF230_H264_mp4_500K.mp4&level=H&transparent=false&bgcolor=%23ffffff&forecolor=%23000000&blockpixel=12&marginblock=1&logourl=&logoshape=no&size=500&kid=cliim&key=42823cde12392cc4c22ddb40c9d9baf2"
          },
          {
            content:"数组",
            images:{id:81,cos_path: "http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4"},
            qrcode:"https://qr.api.cli.im/newqr/create?data=http%253A%252F%252Fclips.vorwaerts-gmbh.de%252Fbig_buck_bunny.mp4&level=H&transparent=false&bgcolor=%23ffffff&forecolor=%23000000&blockpixel=12&marginblock=1&logourl=&logoshape=no&size=500&kid=cliim&key=06c42f3b640375fdc1288de986f17d82"
          }
        ]
    },
    detailcontent:function(){
        var that = this
          this.setData({
              showpage:true,
              showcontent:true,
              showcomment:false,

              customStyle:'height: 70%; background-color: rgba(0,0,0, 0.8)',

          })
    },
    doFavor:function(e){
        if(!this.data.info.token){
            wx.switchTab({
                url: '/pages/wxlogin/wxlogin',
              })
            return}
    
        var newsId = e.currentTarget.dataset.news;
        wx.request({
          url: URL.FavorAPI,
          data: {
            news: newsId
          },
          header: {
            Authorization: this.data.info.token? this.data.info.token : null
          },
          method: 'POST',
          dataType: 'json',
          responseType: 'text',
          success: (res) => {
              
            if(res.statusCode == 200){
                this.setData({
                  ["news.is_favor"]:false,
                  ["news.like"]: this.data.news.like - 1
                })
            }else if(res.statusCode == 201){
              this.setData({
                ["news.is_favor"]: true,
                ["news.like"]: this.data.news.like + 1


              })
            }else{
                wx.showToast({
                  title: '请求错误',
                  icon: 'none'
                })
            }
          }
        })
    
      },

    docollect:function(e){
    if(!this.data.info.token){
        wx.switchTab({
            url: '/pages/wxlogin/wxlogin',
            })
        return}

    var newsId = e.currentTarget.dataset.news;
    wx.request({
        url: URL.collectAPI,
        data: {
        news: newsId
        },
        header: {
        Authorization: this.data.info.token? this.data.info.token : null
        },
        method: 'POST',
        dataType: 'json',
        responseType: 'text',
        success: (res) => {
            
        if(res.statusCode == 200){
            this.setData({
                ["news.is_collect"]:false,
                ["news.collect"]:this.data.news.collect-1,
            })
        }else if(res.statusCode == 201){
            this.setData({
            ["news.is_collect"]: true,
            ["news.collect"]:this.data.news.collect+1,
            })
        }else{
            wx.showToast({
                title: '请求错误',
                icon: 'none'
            })
        }
        }
    })

    },
    onClickPostComment:function(){
        if(!this.data.info.token){
            wx.switchTab({
              url: '/pages/wxlogin/wxlogin',
            })
            
            return}
        if(!this.data.reply.content){
          wx.showToast({
            title: '评论不能为空',
            icon:'loading'
          })
          return
        }
        
        wx.request({
          url: URL.comment,

          data: {
            news:this.data.reply.nid,
            depth: this.data.reply.depth,
            reply: this.data.reply.cid, // 回复的评论id
            content: this.data.reply.content,
            root: this.data.reply.rid
          },
          header: {
            Authorization: this.data.info.token? this.data.info.token : null
          },
          method: 'POST',
          dataType: 'json',
          responseType: 'text',
          success: (res) => {
            if(res.statusCode == 201){
              if (this.data.reply.rootindex == undefined){
                // 如果是根评论，应该添加到
                var dataList = this.data.news.comment;
                dataList.unshift(res.data)
                this.setData({
                  ["news.comment"]: dataList,
                  ["news.comment_count"]:this.data.news.comment_count + 1
                });
                this.onClickCancelCommentModal();
              }else{
                  console.log('rootindex',this.data.reply.rootindex)
                var childCommentList = this.data.news.comment[this.data.reply.rootindex].child;
                if(childCommentList==undefined){
                    childCommentList=[]
                }
                childCommentList.unshift(res.data);
                
                this.setData({
                  ["news.comment[" + this.data.reply.rootindex + "].child"]: childCommentList,
                  ["news.comment_count"]: this.data.news.comment_count + 1
                });
                this.onClickCancelCommentModal();
              }
              
              // 如果是子评论，应该添加到哪里？放在二级评论的最上方
    
            }
          }
        })
    
      },
    inputComment:function(e){
        this.setData({
          ['reply.content']: e.detail.value
        })
    },
    onClickClearReply:function(){
        this.setData({
          reply:{
            depth:1,
            nid: this.data.reply.nid
          }
        })
    },
    onClickShowCommentModal:function(e){

        this.setData({
          isShowCommentModal:true,
          showpage:false,
          reply: e.currentTarget.dataset
        })
    },
    onClickCancelCommentModal:function(){
        this.setData({
          isShowCommentModal: false,
          reply: {}
        })
    },
    showcomment:function(){
          var that = this
          this.setData({
              showpage:true,
              showcomment:true,
              showcontent:false,
              scanbutton:false,
              customStyle:'height: 80%; background-color: rgba(255, 255, 255, 0.9)'
          })

    },
    getMore:function(e){
        var rootId = e.currentTarget.dataset.root;
        var idx = e.currentTarget.dataset.idx;
        /**
         *  http://127.0.0.1:8000/api/commnet/12/
         *  http://127.0.0.1:8000/api/commnet/?root=12
         */
        wx.request({
          url: URL.comment,
          data: {
            root:rootId
          },
          header: {
            Authorization:this.data.info.token? this.data.info.token : null
          },
          method: 'GET',
          dataType: 'json',
          responseType: 'text',
          success: (res) => {
            // 找到跟评论下的child，把child替换为 res.data
            console.log(idx,res.data);
            this.setData({
              ["news.comment["+ idx +"].child"]:res.data
            })
          }
        })
    
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        videoid=options.videoID;
        console.log("videoid",options);
        this.setData({
            codeurl:URL.codeurl+videoid+'/',
        })
        //请求对应ID的video
        wx.request({
          url: URL.classDetail+videoid+'/',
        //   data: data,
        header:{
            Authorization: this.data.info.token? this.data.info.token : null
          },
          dataType: 'json',
          method: 'GET',
          timeout: 0,
          success: (result) => {
              this.setData({
                  news:result.data
              })
            //   this.setData({
            //       news:result.data
            //   })
              console.log('news',this.data.news)
              if(result.data.images[0].cos_path.slice(-3)!='png'){
                  this.setData({
                      videopage:true,
                  })
                  var comlist = result.data.comment
                //   for (var i in comlist){
                //     // console.log('iii',comlist[i])
                //     this.data.danmulist.push({text:comlist[i].content,color:'#000000',time:~~(Math.random() * 6)})
                //     if (comlist[i].child){
                //       for (var x in comlist[i].child){
                //         this.data.danmulist.push({text:comlist[i].child[x].content,color:'#000000',time:~~(Math.random() * 6)})
                //       }
                //     }
                //     else{
                //       console.log(comlist[i].child)
                //     }
                    
                //   }
                //   console.log('ddd',this.data.danmulist)
                //   console.log('dddmmm',this.data.danmu)

                  var videoContext = wx.createVideoContext('myvideo', this);
　　                videoContext.requestFullScreen();

              }else{
                console.log("videooo",videoid)
                  wx.navigateTo({
                    url: '../imagenews/imagenews?videoID='+videoid,
                  })
                  console.log(result.data.images[0].cos_path.slice(-3))
                //   this.setData({
                //       videopage:false
                //   })
              }
          },
          fail: (res) => {
              this.onLoad({videoID:videoid-1})
              wx.showToast({
                title: '没有更多了',
              })
          },
          complete: (res) => {},
        })
    },
    scanclick:function(options){
      console.log('////',this.data.scanbutton)
      this.setData({
      scanbutton:!(this.data.scanbutton)
    })
    },
    loadmore:function(e){
      if(e.detail.source=="touch"){
        this.setData({
          thisindex:e.detail.current,
          scanbutton:false
          
        })
        if(e.detail.current%10==8){
         
        }
      }
    },
    nextclass:function(){
      this.onLoad({videoID:videoid-1})
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
        var videoid = this.data.news.videoID+1
        wx.showToast({
          title: '下一页',
          
        })
        wx.navigateTo({
          url: '/pages/video/video?videoID={{videoid}}',
          success: (result) => {},
          fail: (res) => {
              wx.showToast({
                title: '网络请求错误',
                icon: 'loading',
              })
          },
          complete: (res) => {},
        })
    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },
    priviewpic:function(){
        wx.previewImage({
            current: this.data.codeurl, // 当前显示图片的http链接
            urls: [this.data.codeurl] // 需要预览的图片http链接列表
          })
    },
    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})

// // pages/imagenews/imagenews.js
// var URL = require("../../config/api")
// Page({

//     /**
//      * 页面的初始数据
//      */
//     data: {
//         news:null,
//         videopage:false,
//     },
//     onClickPostComment:function(){
//         if(!this.data.reply.content){
//           wx.showToast({
//             title: '评论不能为空',
//             icon:'loading'
//           })
//           return
//         }
        
//         wx.request({
//           url: api.CommentAPI,

//           data: {
//             news:this.data.reply.nid,
//             depth: this.data.reply.depth,
//             reply: this.data.reply.cid, // 回复的评论id
//             content: this.data.reply.content,
//             root: this.data.reply.rid
//           },
//           method: 'POST',
//           dataType: 'json',
//           responseType: 'text',
//           success: (res) => {
//             if(res.statusCode == 201){
//               if (this.data.reply.rootindex == undefined){
//                 // 如果是根评论，应该添加到
//                 var dataList = this.data.news.comment;
//                 dataList.unshift(res.data)
//                 this.setData({
//                   ["news.comment"]: dataList,
//                   ["news.comment_count"]:this.data.news.comment_count + 1
//                 });
//                 this.onClickCancelCommentModal();
//               }else{
//                 var childCommentList = this.data.news.comment[this.data.reply.rootindex].child;
//                 childCommentList.unshift(res.data);
//                 this.setData({
//                   ["news.comment[" + this.data.reply.rootindex + "].child"]: childCommentList,
//                   ["news.comment_count"]: this.data.news.comment_count + 1
//                 });
//                 this.onClickCancelCommentModal();
//               }
              
//               // 如果是子评论，应该添加到哪里？放在二级评论的最上方
    
//             }
//           }
//         })
    
//       },
//       inputComment:function(e){
//         this.setData({
//           ['reply.content']: e.detail.value
//         })
//       },
//       onClickClearReply:function(){
//         this.setData({
//           reply:{
//             depth:1,
//             nid: this.data.reply.nid
//           }
//         })
//       },
//       onClickShowCommentModal:function(e){
//         this.setData({
//           isShowCommentModal:true,
//           reply: e.currentTarget.dataset
//         })
//       },
//       onClickCancelCommentModal:function(){
//         this.setData({
//           isShowCommentModal: false,
//           reply: {}
//         })
//       },
//     /**
//      * 生命周期函数--监听页面加载
//      */
//     onLoad: function (options) {
//         var videoid=options.videoID;
//         console.log('img',videoid);
//         //请求对应ID的video
//         wx.request({
//           url: URL.classDetail+videoid+'/',
//         //   data: data,
//           dataType: 'json',
//           method: 'GET',
//           responseType: 'text',
//           timeout: 0,
//           success: (result) => {
//               console.log(result)
//               this.setData({
//                   news:result.data
//               })
//                   console.log(result.data.images[0].cos_path.slice(-3))
//                   this.setData({
//                       videopage:false
//                   })
              
//           },
//           fail: (res) => {},
//           complete: (res) => {},
//         })
//     },

//     /**
//      * 生命周期函数--监听页面初次渲染完成
//      */
//     onReady: function () {

//     },

//     /**
//      * 生命周期函数--监听页面显示
//      */
//     onShow: function () {

//     },

//     /**
//      * 生命周期函数--监听页面隐藏
//      */
//     onHide: function () {

//     },

//     /**
//      * 生命周期函数--监听页面卸载
//      */
//     onUnload: function () {
//       wx.reLaunch({
//         url: '../entry/entry',
//         success: (res) => {},
//         fail: (res) => {},
//         complete: (res) => {},
//       })

//     },
//     getMore:function(e){
//         var rootId = e.currentTarget.dataset.root;
//         var idx = e.currentTarget.dataset.idx;
//         /**
//          *  http://127.0.0.1:8000/api/commnet/12/
//          *  http://127.0.0.1:8000/api/commnet/?root=12
//          */
//         wx.request({
//           url: URL.indexURL,
//           data: {
//             root:rootId
//           },
//           method: 'GET',
//           dataType: 'json',
//           responseType: 'text',
//           success: (res) => {
//             // 找到跟评论下的child，把child替换为 res.data
//             console.log(idx,res.data);
//             this.setData({
//               ["news.comment["+ idx +"].child"]:res.data
//             })
//           }
//         })
    
//       },

//     /**
//      * 页面相关事件处理函数--监听用户下拉动作
//      */
//     onPullDownRefresh: function () {

//     },

//     /**
//      * 页面上拉触底事件的处理函数
//      */
//     onReachBottom: function () {

//     },

//     /**
//      * 用户点击右上角分享
//      */
//     onShareAppMessage: function () {

//     }
// })