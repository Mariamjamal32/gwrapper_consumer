#!/bash/bin
export TESTAPP=gwrapper_consumer_web
export BRANCH=master
# docker build --no-cache -t wrapperapp ${BRANCH:+--build-arg BRANCH=master} - <<< "FROM $TESTAPP"
docker build --no-cache -t wrapper_child_app_docker_setup ${BRANCH:+--build-arg BRANCH=$BRANCH} - <<< "FROM $TESTAPP" 1>&2
