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

function getImage(data) {
    return '<img style="width:100%;" src="data:image/png;base64,'+ data +'">';
}

function resetImage() {
    $('#iframe-image').html("<br><br><br><br><h4 style=\"text-align: center;color:orange;vertical-align: middle;\"><em>--- Your graph will be shown here ---</em></h4>");
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
            $('#iframe-image').html('<p>640 x 480</p>' + getImage(data));
            $(".input-vals").val("");
        }

    })
});



function getKruskal() {
    $.ajax({
        url: "getKruskal",
        type: "POST",
        success: function (data) {
            $('#iframe-image').html('<p>640 x 480</p>' + getImage(data));
        }
    });
}

function getPrims() {
    $.ajax({
        url: "getPrims",
        type: "POST",
        success: function (data) {
            $('#iframe-image').html('<p>640 x 480</p>' + getImage(data));
        }
    });
}

function resetGraph() {
    $.ajax({
        url: "resetGraph",
        type: "POST",
        success: function (data) {
            resetImage();
        }
    });
}

// <iframe src="" style="height: 480px; width:100%;" title="Iframe result"></iframe>

