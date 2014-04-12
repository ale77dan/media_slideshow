gl.setup(1920, 1080)

local template = 'default'

util.data_mapper{
    ["template"] = function(var)
        template = var
    end
}

function node.render()
    if template == "default" then
        resource.render_child("child1"):draw(0, 0, 1920, 260)
        resource.render_child("child2"):draw(0, 260, WIDTH, HEIGHT)
    elseif template == "fullscreen" then
         resource.render_child("child3"):draw(0, 0, WIDTH, HEIGHT)
    end
end