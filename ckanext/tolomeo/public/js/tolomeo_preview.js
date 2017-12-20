// TOLOMEO preview module
ckan.module('tolomeopreview', function (jQuery, _) {
    return {
        initialize: function () {
            var self = this;

            self.el.empty();
            self.el.append($('<div></div>').attr('id', 'mappa'));

            tolomeo = new TolomeoExt.ToloPanelInter({
//                layout: 'fit',
                withDataPanel: false,
                withToolsPanel: false,
                toolbarOpt: {
                    withPanArrows: true,
                    withQuery: false,
                    withAnnullaSeleziona: false,
                    withSeleziona: false,
                    withIdentify: false,
                    withLegenda: false,
                    withNuovo: false,
                    withUpdateAlfa: false,
                    withAdd: false,
                    withSubtract: false,
                    withAddSub: false,
                    withVertexEdit: false,
                    withDragDrop: false,
                    withDelete: false,
                    withShowCoordinate: false,
                    iconBasePath: TolomeoExt.Vars.TOLOMEOServer + '/tolomeo/img/icone/24-default/',
                    defaults: {scale: 'medium'}
                }
            })

            new Ext.Panel({
                width: 888,
                height: 400,
                layout: 'fit',
                cls: 'clearCSS',
                renderTo: 'mappa',
                items: [tolomeo]
            });

        }
    };
});
