Number.prototype.formatMoney = function (c, d, t) {
    var n = this,
        c = isNaN(c = Math.abs(c)) ? 2 : c,
        d = d == undefined ? "." : d,
        t = t == undefined ? "," : t,
        s = n < 0 ? "-" : "",
        i = String(parseInt(n = Math.abs(Number(n) || 0).toFixed(c))),
        j = (j = i.length) > 3 ? j % 3 : 0;
    return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};

$(document).ready(function () {
    $("#submitButton").click(function () {
        var postBody = {
            make: $("#make").val(),
            model: $("#model").val(),
            year: $("#year").val(),
            mileage: $("#mileage").val(),
            transmission: $("#transmission").val(),
            state: $("#state").val(),
        }

        $.ajax({
            type: "POST",
            url: '/api/predict',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            async: false,
            data: JSON.stringify(postBody),
            success: function (data) {
                var price = parseFloat(data.price);
                var displayPrice = price.formatMoney(2);
                var resultHtml = "<h1>Prediction:</h1><h3>$" + displayPrice + "</h3>";
                $("#resultsSection").html(resultHtml);
            }
        })
    });
});