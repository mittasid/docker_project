$(document).ready(function () {
    var table = $('#movieInfo').DataTable
        ({
            "paging": true,
            ajax: {
                url: "http://localhost:5000/",
                dataSrc: "",
            },
            "columns"
            : [
                { "data": "name" },
                { "data": "rating"}
            ],
    });
var table = $('#movieInfo').DataTable();
});
