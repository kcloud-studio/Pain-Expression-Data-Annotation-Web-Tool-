var url = '/changephoto/'
function changedate(){
    var data = {
        'change': "get_new_url"
    }
    $.ajax({
        type: 'get',
        url: url,
        data: data,                   // 要传给后台的数据
        dataType: 'json',             // 数据格式
        success: function (data) {
            alert(data)
            document.getElementById("photo").src = data
        }
    });
}


