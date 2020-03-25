This app is ported from tinkerit to dash to monitor all the logs of PLTCM 
    #celery -A worker worker --loglevel=debug
        # at worker side:
        # set $env:FORKED_BY_MULTIPROCESSING = 1
        # then
        # celery -A myworker worker --loglevel=info
        # done!
		# $env:FORKED_BY_MULTIPROCESSING = 1; celery -A tasks worker --loglevel=info
		# $env:FORKED_BY_MULTIPROCESSING = 1; celery -A tasks beat --loglevel=info

        # python index.pyc
        # celery -A tasks worker -l info -P gevent
        # $env:FORKED_BY_MULTIPROCESSING = 1; celery -A tasks beat --loglevel=info
        # Delete celerybeat-schedule.bak if any from the dir
        # Delete celerybeat-schedule.dat if any from the dir
        # Delete celerybeat-schedule.dir if any from dir 


        
         