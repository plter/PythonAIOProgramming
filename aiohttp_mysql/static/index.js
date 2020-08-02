(function () {
    $(".btn-delete-item").click(function (e) {
        if (!confirm("你真的要删除这条数据吗？")) {
            e.preventDefault();
        }
    });
})();
