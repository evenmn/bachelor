def rk4(x, v, a, dt, b=0):
        x1 = x
        v1 = v
        a1 = a(x1, v1, 0, b)

        x2 = x + 0.5*v1*dt
        v2 = v + 0.5*a1*dt
        a2 = a(x2, v2, dt/2.0, b)

        x3 = x + 0.5*v2*dt
        v3 = v + 0.5*a2*dt
        a3 = a(x3, v3, dt/2.0, b)

        x4 = x + v3*dt
        v4 = v + a3*dt
        a4 = a(x4, v4, dt, b)

        xEnd = x + (dt/6.0)*(v1 + 2*v2 + 2*v3 + v4)
        vEnd = v + (dt/6.0)*(a1 + 2*a2 + 2*a3 + a4)

        return xEnd, vEnd
