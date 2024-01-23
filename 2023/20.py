data = """%tx -> dx
%nx -> fn, rn
%nr -> cj, mh
%nk -> jt, vk
%mv -> fk, rn
&pz -> kt, pg, mb, vr, hp, jp, tx
&jt -> fb, zb, jq, sv, lp
%vp -> lp, jt
&qs -> gf
%lj -> jt, dt
%jh -> mh
%xc -> nx
%hx -> xb
%kd -> pz, pp
%jq -> jt, qt
%lp -> jm
%ph -> mb, pz
&sv -> gf
%ff -> xc
%th -> mh, hx
%kt -> ct
%ct -> kd, pz
&mh -> bc, qs, hx, xb, nv
&pg -> gf
%fn -> kn
%sk -> hr
%nv -> mh, th
%dx -> pz, ph
broadcaster -> bx, jq, nv, jp
%dt -> jt, zb
%fx -> sk, rn
%rv -> rn
%gv -> mh, nr
%fk -> rn, rv
%cj -> mh, vh
%xk -> jt, nk
%vh -> mh, jh
%zb -> fb
%mb -> jc
%kn -> rn, mv
%jc -> pz, kt
&sp -> gf
%hp -> tx
%jf -> bc, mh
%fb -> vp
%xm -> mh, gv
%jm -> jt, xk
%vr -> hp
%hr -> ff
%jp -> pz, vr
&rn -> fn, hr, bx, ff, xc, sp, sk
%pp -> pz
&gf -> rx
%xb -> jf
%bx -> rn, fx
%bc -> xm
%qt -> lj, jt
%vk -> jt""".split('\n')


from copy import deepcopy
from math import lcm

orig_config = {} # name to (module_type, list of next steps)
orig_flipflop = {} # name to status (0 for off, 1 for on)
orig_last_sent =  {} # receiver to sender to status (0 for low, 1 for high)
for line in data:
    src, dest = line.split(' -> ')
    dest = dest.split(', ')
    module = None
    if src[0] == '%':
        module = src[0]
        name = src[1:]
        orig_flipflop[name] = 0
    elif src[0] == '&':
        module = src[0]
        name = src[1:]
    else:
        module = None
        name = src

    orig_config[name] = (module, dest)
    # Check sending to conjunction
    for d in dest:
        if d in orig_last_sent:
            orig_last_sent[d][name] = 0
        else:
            orig_last_sent[d] = { name : 0 }

#####
sums = [0, 0]
config = deepcopy(orig_config)
flipflop = deepcopy(orig_flipflop)
last_sent = deepcopy(orig_last_sent)
for i in range(1000):
    queue = [('broadcaster', 0)]
    sums[0] += 1
    while queue:
        src, status = queue.pop(0)
        if src == 'output' or src not in config:
            continue

        module, dest = config[src]

        if module == '%':
            if status == 1:
                continue
            flipflop[src] = (flipflop[src] + 1) % 2
            status = flipflop[src]
        elif module == '&':
            for sender in last_sent[src]:
                if last_sent[src][sender] == 0:
                    status = 1
                    break
            else:
                status = 0

        for d in dest:
            last_sent[d][src] = status
            sums[status] += 1
            queue.append((d, status))
print(sums[0] * sums[1])

#####
config = deepcopy(orig_config)
flipflop = deepcopy(orig_flipflop)
last_sent = deepcopy(orig_last_sent)
result = { 'qs': None, 'sv': None, 'pg': None, 'sp': None }
for i in range(10000):
    queue = [('broadcaster', 0)]
    sums[0] += 1
    while queue:
        src, status = queue.pop(0)
        if src == 'output' or src not in config:
            continue

        module, dest = config[src]

        if module == '%':
            if status == 1:
                continue
            flipflop[src] = (flipflop[src] + 1) % 2
            status = flipflop[src]
        elif module == '&':
            for sender in last_sent[src]:
                if last_sent[src][sender] == 0:
                    status = 1
                    break
            else:
                status = 0

        for d in dest:
            last_sent[d][src] = status
            sums[status] += 1    
            if d == 'gf' and not result[src] and status == 1:
                result[src] = i + 1
            queue.append((d, status))
    if None not in result.values():
        break
print(lcm(*list(result.values())))
