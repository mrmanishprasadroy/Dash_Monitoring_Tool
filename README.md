This app is ported from tinkerit to dash to monitor all the logs of PLTCM 
# Starting Celery and Celery Beat
        # at worker side:
        # set $env:FORKED_BY_MULTIPROCESSING = 1
        # then
        # celery -A myworker worker --loglevel=info
# Single line command for powershell 
		# $env:FORKED_BY_MULTIPROCESSING = 1; celery -A tasks worker --loglevel=info
		# $env:FORKED_BY_MULTIPROCESSING = 1; celery -A tasks beat --loglevel=info
# use gevent incase $env:FORKED_BY_MULTIPROCESSING = 1 failure 
        # python index.py
        # celery -A tasks worker -l info -P gevent
        # $env:FORKED_BY_MULTIPROCESSING = 1; celery -A tasks beat --loglevel=info



# Expermental FLower Dash Board
    # celery flower -A tasks --address=127.0.0.1 --port=5555

