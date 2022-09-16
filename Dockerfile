FROM python:3.10.2-slim
ADD . /app
WORKDIR /app
RUN pip install flask \
    pip install mysql-connector-python
RUN mkdir azagent;cd azagent;curl -fkSL -o vstsagent.tar.gz https://vstsagentpackage.azureedge.net/agent/2.210.1/vsts-agent-linux-x64-2.210.1.tar.gz;tar -zxvf vstsagent.tar.gz; if [ -x "$(command -v systemctl)" ]; then ./config.sh --environment --environmentname "b-envrion" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/jiyoungsung799/ --work _work --projectname 'myproject' --auth PAT --token c7xadhoopssbedbnrchnito2zodeshq72j2yezfqrkcjt242hj7a --runasservice; sudo ./svc.sh install; sudo ./svc.sh start; else ./config.sh --environment --environmentname "b-envrion" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/jiyoungsung799/ --work _work --projectname 'myproject' --auth PAT --token c7xadhoopssbedbnrchnito2zodeshq72j2yezfqrkcjt242hj7a; ./run.sh; fi
ENTRYPOINT python app.py