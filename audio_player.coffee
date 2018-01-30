# from github user dmitriy-serdyuk

import * as p from "core/properties"
import {Widget, WidgetView} from "models/widgets/widget"

export class AudioPlayerView extends WidgetView
    initialize: (options) ->
        super(options)
        @get_data()
        @connect(@model.data_source.change, () => @get_data())

    get_data: () ->
        @el.innerHtml = ""

        source = @model.data_source
        for i in [0...source.get_length()]
          @create_player(source.get_column('data')[i])

    create_player: (source) ->
        audio = document.createElement("audio")
        audio.setAttribute("controls", "controls")
        audio.setAttribute("src", source)
        audio.load()
        p = document.createElement("p")
        @el.appendChild(p)
        @el.appendChild(audio)


export class AudioPlayer extends Widget
    type: "AudioPlayer"
    default_view: AudioPlayerView

    @define {
        data_source: [p.Instance, ]
    }
