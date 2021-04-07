function showAddEdgeForm() {
    $("#add-edge-control").prop("disabled", true);
    $("#add-edge-form-div").fadeIn(() => {
        $("#a-val").focus();
    });
}

function hideForm() {
    $("#add-edge-control").prop("disabled", false);
    $(".input-vals").val("");
    $("#add-edge-form-div").fadeOut();
}

$("#add-edge-form").submit(function (e) { 
    e.preventDefault();
    let a = document.getElementById("a-val").value;
    let b = document.getElementById("b-val").value;
    let w = document.getElementById("w-val").value;

    $.ajax({
        url: "addEdge",
        type: "POST",
        data: JSON.stringify({ a:a, b:b, weight: w }),
        contentType: "application/json",
        success: function (data) {
            $('#iframe-image').html('<p>640 x 480</p><img src="data:image/png;base64,'+ data +'">');
            $(".input-vals").val("");
        }

    })
});



function getKruskal() {
    $.ajax({
        url: "getKruskal",
        type: "POST",
        success: function (data) {
            $('#iframe-image').html('<p>640 x 480</p><img src="data:image/png;base64,'+ data +'">');
        }
    });
}

function getPrims() {
    $.ajax({
        url: "getPrims",
        type: "POST",
        success: function (data) {
            $('#iframe-image').html(
                '<p>640 x 480</p>'+
                '<img src="data:image/png;base64,'+ data +'">'
            );
        }
    });
}

// <iframe src="" style="height: 480px; width:100%;" title="Iframe result"></iframe>

