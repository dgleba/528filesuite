def create_ctx():
    password = getpass.getpass("password: ")

    kwargs = {
        "password": password,
    }

    ctx = Connection(host='192.168.88.64', user='albe', connect_kwargs=kwargs)

    return ctx

@task
def two(ctx):
    
    ctx = create_ctx() # replace original `ctx` with own `ctx`

    print(ctx)
    
    print('connect_kwargs:', ctx['connect_kwargs'])
    print('user:', ctx['user'])
    
    print('sudo user:', ctx['sudo']['user'])
    print('sudo password:', ctx['sudo']['password'])
          
    #ctx.run('uname -a')
    #ctx.run('whoami')
    #ctx.sudo('whoami')