var filesPane;

$(function() {
    var layout_config = {
        content: [{
            type: "row",
            content: [{
                type: "component",
                componentName: "files",
                width: 25,
                isClosable: false,
            }, {
                type: "column",
                content: [{
                    type: "stack",
                    isClosable: false,
                    content: [],
                }, {
                    type: "stack",
                    id: "terminal",
                    height: 30,
                    isClosable: false,
                    content: [],
                }],
            }],
        }],
    };

    var layout = new GoldenLayout(layout_config, $("#editor-container"));


    layout.registerComponent("files", function(container, componentState) {
        filesPane = new FilesPane(
            container.getElement(),
            ws_endpoints.file_monitor,
            {
                openFile: function(fname) {
                    console.log(fname);
                },
            },
        );
    });

    layout.registerComponent("file", function(container, componentState) {
    });


    layout.init();
    $(window).resize(function() {
        layout.updateSize();
    });
});
