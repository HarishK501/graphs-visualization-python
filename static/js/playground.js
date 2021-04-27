function showAddEdgeForm() {
    $("#add-edge-control").prop("disabled", true);
    $("#add-edge-form-div").fadeIn(() => {
        $("#a-val").focus();
    });
}

function showDijkstraForm() {
    $("#dijkstra-control").prop("disabled", true);
    $("#dijkstra-form-div").fadeIn(() => {
        $("#s1-val").focus();
    });
}

function hideForm(choice) {
    if (choice == 1) {
        $("#add-edge-control").prop("disabled", false);
        $(".input-vals").val("");
        $("#add-edge-form-div").fadeOut();
    } else if (choice == 2) {
        $("#dijkstra-control").prop("disabled", false);
        $(".input-vals").val("");
        $("#dijkstra-form-div").fadeOut();
    }
}

function updateNodesDropdownMenu(){
    $.ajax({
        url: "getNodes",
        type: "POST",
        success: function (data) {
            let options = "<option selected disabled hidden style='display: none' value=''></option>";
            for(let i=0; i < data['nodes'].length; i++) {
                options += '<option value="'+ String(data['nodes'][i]) +'">'+ String(data['nodes'][i]) +'</option>'
            }
            $(".nodes-dropdown").html(options);
        },
    });
}

function getImage(data) {
    return '<img style="width:100%;" src="data:image/png;base64,' + data + '">';
}

function resetImage() {
    $("#iframe-image").html(
        '<br><br><br><br><h4 style="text-align: center;color:orange;vertical-align: middle;"><em>--- Your graph will be shown here ---</em></h4>'
    );
}

$("#add-edge-form").submit(function (e) {
    e.preventDefault();
    let a = document.getElementById("a-val").value;
    let b = document.getElementById("b-val").value;
    let w = document.getElementById("w-val").value;

    $.ajax({
        url: "addEdge",
        type: "POST",
        data: JSON.stringify({ a: a, b: b, weight: w }),
        contentType: "application/json",
        success: function (data) {
            $("#iframe-image").html("<p>640 x 480</p>" + getImage(data));
            $(".input-vals").val("");
            $("#result-text").html("");
            updateNodesDropdownMenu();
        },
    });
});

$("#dijkstra-form").submit(function (e) {
    e.preventDefault();
    let s1 = document.getElementById("s1-val").value;
    let s2 = document.getElementById("s2-val").value;

    if (s1 == s2) {
        alert("Source and destination are same!");
    }
    else {
        $.ajax({
            url: "dijkstra",
            type: "POST",
            data: JSON.stringify({ src: s1, dest: s2 }),
            contentType: "application/json",
            success: function (data) {
                $("#iframe-image").html("<h4>Dijkstra's shortest path</h4><br>" + getImage(data));
                $(".input-vals").val("");
            },
        });
    }

    
});

function getKruskal() {
    $.ajax({
        url: "getKruskal",
        type: "POST",
        success: function (data) {
            // console.log(data['text']);
            $("#iframe-image").html("<h4>Kruskal's MST</h4><br>" + getImage(data['img']));
            let resultTextHeader = "<h4>Steps</h4><br>"
            $("#result-text").html(resultTextHeader+data['text']);
            
        },
    });
}

function getPrims() {
    $.ajax({
        url: "getPrims",
        type: "POST",
        success: function (data) {
            $("#iframe-image").html("<h4>Prim's MST</h4><br>" + getImage(data['img']));
            let resultTextHeader = "<h4>Steps</h4><br>"
            $("#result-text").html(resultTextHeader+data['text']);
        },
    });
}

function resetGraph() {
    $.ajax({
        url: "resetGraph",
        type: "POST",
        success: function (data) {
            resetImage();
            $(".input-vals").val("");
            $("#result-text").html("");
            updateNodesDropdownMenu();
        },
    });
}
