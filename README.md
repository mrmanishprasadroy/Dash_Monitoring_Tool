This app is ported from tinkerit to dash to monitor all the logs of PLTCM 
    #celery -A worker worker --loglevel=debug
        # at worker side:
        # set $env:FORKED_BY_MULTIPROCESSING = 1
        # then
        # celery -A myworker worker --loglevel=info
        # done!
		# $env:FORKED_BY_MULTIPROCESSING = 1; celery -A tasks worker --loglevel=info
		# $env:FORKED_BY_MULTIPROCESSING = 1; celery -A tasks beat --loglevel=info
