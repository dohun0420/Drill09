# world = [] 단일 계층 구조
world = [ [], [], [] ]

def add_object(o, depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for o in world:
        for layer in world:
            for o in layer:
                o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 지운는 미션은 달성, 없을 시 레이어 만큼 계속 반복

    print('에러 : 존재하지 않은 객체를 지운다고?')