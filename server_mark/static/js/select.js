function changeword()
{
    var a = new Array("要你点你还真的点？傻？再来点一次！","woc！你还真的又点了呀","好了不闹了 告辞");
    var b = new Array("要你点你还真的点？傻？再来点一次！","woc！你还点了呀","好了不闹了");
  x_r = document.getElementById("u");
  x_l = document.getElementById("u");
 if(xx<3){
 x_r.innerHTML = a[xx++];
 x_l.innerHTML = b[xx++];
}
 //上面这句话会使得你要连续按3次按钮才会结束button里的值变化
}
