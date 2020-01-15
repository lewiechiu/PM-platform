$(
    function() {
        $("#test-table").FullTable({
            "alwaysCreating":true,
            "selectable":true,
            "fields": {
                "name":{
                    "mandatory":true,
                    "errors":{
                        "mandatory":"First name is mandatory"
                    }
                },
                "company":{
                    "mandatory":true,
                    "errors":{
                        "mandatory":"Company name is mandatory"
                    }
                }
            }
        });
        $("#test-table-add-row").click(function() {
            $("#test-table").FullTable("addRow");
        });
        $("#test-table-get-value").click(function() {
            console.log($("#test-table").FullTable("getData"));
        });
        $("#test-table").FullTable("on", "error", function(errors) {
            for (var error in errors) {
                error = errors[error];
                console.log(error);
            }
        });
        $("#test-table").FullTable("draw");
    }
);