/**
 * Created by admin on 2017/1/5.
 */

$('#tipModal').on('hide.bs.modal',function(){
    location.reload()
});

$('#add').on('click',function(){
        var hostname = $('#hostname').val();
        var ip = $('#ip').val();
        var idc = $('#idc').val();
        var cabinet = $('#cabinet').val();
        var remark = $('#remark').val();

        $.ajax({
            url:"/addserver/",
            type:'POST',
            data:{hostname:hostname,ip:ip,idc:idc,cabinet:cabinet,remark:remark},
            success:function(data){
                if (data=='ok') {
                    $('#addserver').modal('hide');
                    swal({
                          title: "添加成功",
                          type: "success",
                          text: "添加信息:"+hostname,
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

//查看数据获取数据信息
var editserver=function(id){
    $.ajax({
            url:"/editserver/?id="+id,
            type:'GET',
            success:function(data){
                data = JSON.parse(data);
                if (data.code=='0') {
                    var server = JSON.parse(data.server)[0].fields;
                    $("#update_id").val(id);
                    $("#update_hostname").val(server.hostname);
                    $("#update_ip").val(server.ip);
                    $("#update_idc").val(server.idc);
                    $("#update_cabinet").val(server.cabinet);
                    $("#update_remark").val(server.remark);
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
        var hostname = $('#update_hostname').val();
        var ip = $('#update_ip').val();
        var idc = $('#update_idc').val();
        var cabinet = $('#update_cabinet').val();
        var remark = $('#update_remark').val();

        $.ajax({
            url:"/updateserver/",
            type:'POST',
            data:{id:id,hostname:hostname,ip:ip,idc:idc,cabinet:cabinet,remark:remark},
            success:function(data){
                if (data=='ok') {
                    $('#updateserver').modal('hide');
                    swal({
                          title: "更新成功",
                          type: "success",
                          text: "更新信息:"+hostname,
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




