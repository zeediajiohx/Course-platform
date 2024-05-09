// component/tabbar/tabbar.js
var app = getApp()
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    selected:{
      type:Number,
      value:0
    },
    showrelease:{
        type:Boolean,
        value:false
    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    color: "#7A7E83",
    selectedColor: "#DC143C",
    list: [
        {
      pagePath: "/pages/entry/entry",
      text: "首页"
    }, {
        pagePath:"/pages/release/release",
      text: "发布"
    }, 
    {
      pagePath: "/pages/wxlogin/wxlogin",
      text: "我的"
    }
],
    list1: [
        {
        pagePath: "/pages/entry/entry",
        text: "首页"
      },
      {
        pagePath: "/pages/wxlogin/wxlogin",
        text: "我的"
      }
    ]
  },

  /**
   * 组件的方法列表
   */
  methods: {
    
    switchTab(e) {
      var data = e.currentTarget.dataset
      var url = data.path;
      if(url){
        wx.switchTab({ url });
        // if(wx.getStorageSync('userInfo').ismanager){
        //     this.setData({
        //         list1:[
        //          {
        //        pagePath: "/pages/entry/entry",
        //        text: "首页"
        //      }, {
        //          pagePath:"/pages/release/release",
        //        text: "发布"
        //      }, 
        //      {
        //        pagePath: "/pages/wxlogin/wxlogin",
        //        text: "我的"
        //      }
        //  ]
        //     })
        // }else{
        //     this.setData({
        //         list1:[
        //          {
        //          pagePath: "/pages/entry/entry",
        //          text: "首页"
        //        },
        //        {
        //          pagePath: "/pages/wxlogin/wxlogin",
        //          text: "我的"
        //        }
        //      ]
        //     })
        // }
      }else{
        

      }

      
    },
    
  },
//   attached:function(){
//    if(wx.getStorageSync('userInfo').ismanager){
//        this.setData({
//            list1:[
//             {
//           pagePath: "/pages/entry/entry",
//           text: "首页"
//         }, {
//             pagePath:"/pages/release/release",
//           text: "发布"
//         }, 
//         {
//           pagePath: "/pages/wxlogin/wxlogin",
//           text: "我的"
//         }
//     ]
//        })
//    }else{
//        this.setData({
//            list1:[
//             {
//             pagePath: "/pages/entry/entry",
//             text: "首页"
//           },
//           {
//             pagePath: "/pages/wxlogin/wxlogin",
//             text: "我的"
//           }
//         ]
//        })
//    }
//   }
  
})
