var url_data = '/change_photo/';   //指向获取图片url的虚拟地址
var url_time = '/time/';           //指向获取时间戳的虚拟地址
var url_end = '/tag_end/';         //指向跳转页面
var url_tagging = '/tagging/';     //指向标注页面
var url_datainput ='/dataset/';    //指向数据集发送的虚拟地址
var url_obj ='/object_name/';      //指向获取对象名的虚拟地址
var photo_data = "";
var time_stamp = "";
var obj_name = "";
var xx = 0;
var count01 = 0;
var count02 = 0;

    function photo(){             //获取图片url
            $.ajax({
                async:false,
                url:url_data,
                type:'get',
                success:function (data) {
                    photo_data = data
                },
                dataType:'text'
            });
            return photo_data
    }



    function photo_time(){                //获取服务器端时间戳
            $.ajax({
                async:false,
                url:url_time,
                type:'get',
                success:function (data) {
                    time_stamp = data
                },
                dataType:'text'
            });
            return time_stamp
    }



    function obj_name_fun(){              //获取图片对象名
            $.ajax({
                async:false,
                url:url_obj,
                type:'get',
                success:function (data) {
                    obj_name = data
                },
                dataType:'text'
            });
            return obj_name
    }


    function fun01() {
        photo()
        photo_time()
        obj_name_fun()
        document.getElementById("baby_face").src = photo();
        document.getElementById("touchtostart").style.display="none";
        document.getElementById("first_text").innerHTML = "标注中";
        document.getElementById("nameoftagging").innerHTML = "标注中。。。";
        document.getElementById("column1").innerHTML = "图片可用";
        document.getElementById("column2").innerHTML = "图片不可用";
        }



function changeword()
{
    var a = new Array("有皱眉","002","有挤眼","004","有鼻唇沟加深","006","有张口","008","有嘴垂直伸展","010","有嘴水平伸展","012","有舌呈杯状","014","有下颌颤动","016","有嘴呈“O”型","018");
    var b = new Array("001","无皱眉","003","无挤眼","005","无鼻唇沟加深","007","无张口","009","无嘴垂直伸展","011","无嘴水平伸展","013","无舌呈杯状","015","无下颌颤动","017","无嘴呈“O”型","019");
  x_r = document.getElementById("column1");
  x_l = document.getElementById("column2");
 if(xx<18){
 x_r.innerHTML = a[xx++];
 x_l.innerHTML = b[xx++];
    }else{
     window.location.href= url_end;  //转跳页面至选择步骤
     post_data_inport()
   }
 //在两个字符集中，交替显示内容
}


function count_yes() {
            count01 ++;    //注意！！！此处逻辑上要减2
            return count01
        }



function count_no() {
            count02 ++;    //注意，此处逻辑上不需要处理
            return count02
        }



function error_count() {        //此函数用于图片异常情况的逻辑
        if (xx == 2){
            window.location.href= url_tagging;
            alert("系统将重新加载")
        }
}



function post_data_inport() {
         $.ajax({
         type: "POST",
         url:url_datainput,
         contentType: "application/json;charset=utf-8",
         data: JSON.stringify({"data_yes":count_yes(),"data_no":count_no(),"time":photo_time(),"obj_name":obj_name_fun()}),
         success: function (data) {
             alert("提交成功")
         }
     });
}