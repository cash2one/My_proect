/**
 * Created by Administrator on 2017/1/10.
 */

$('#save_idc').on('click',function(){
        var name = $('#name').val();
        var address = $('#address').val();

        $.ajax({
            url:"/addidc/",
            type:'POST',
            data:{name:name,address:address},
            success:function(data){
                if (data=='ok') {
                    $('#create_idc').modal('hide');
                    swal({
                          title: "添加成功",
                          type: "success",
                          text: "添加信息:"+name,
                          timer: 2000,
                          showConfirmButton: false
                    })
                }else{
                    alert('error')
                }
                window.location.reload();
            }
        })
});

//查看数据获取数据信息
var editidc=function(id){
    $.ajax({
            url:"/editidc/?id="+id,
            type:'GET',
            success:function(data){
                data = JSON.parse(data);
                if (data.code=='0') {
                    var idc = JSON.parse(data.idc)[0].fields;
                    $("#update_id").val(id);
                    $("#update_name").val(idc.name);
                    $("#update_address").val(idc.address);
                }else{
                    alert('error1')
                }
            },
            error:function(data){
                alert("error2")
            }

        })
}

//更新数据
$('#update').on('click',function(){

        var id = $('#update_id').val();
        var name = $('#update_name').val();
        var address = $('#update_address').val();

        $.ajax({
            url:"/updateidc/",
            type:'POST',
            data:{id:id,name:name,address:address},
            success:function(data){
                if (data=='ok') {
                    $('#updateidc').modal('hide');
                    swal({
                          title: "更新成功",
                          type: "success",
                          text: "更新信息:"+name,
                          timer: 2000,
                          showConfirmButton: false
                    })
                }else{
                    alert('error')
                }
                window.location.href=window.location.href;
            }
        })
});
