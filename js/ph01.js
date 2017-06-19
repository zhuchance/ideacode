/**
 * Created by chance on 2017/6/16.
 */

var page = require('webpage').create();
page.open('http://www.baidu.com', function () {
// page.open('http://xinsheng.huawei.com', function () {
    // page.render('baidu.png');
    page.render('xinsheng.png');
    phantom.exit();
});