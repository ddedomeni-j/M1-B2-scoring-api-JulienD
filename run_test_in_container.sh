
docker run --rm \
  -v "/$(PWD)/tests:/home/appuser/app/tests" \
  --entrypoint sh \
  pyrenex-risk-api:v0.1.0 \
  -c "ls -R /home/appuser/app/tests"

docker run --rm \
  -v /$(PWD)/tests:/home/appuser/app/tests \
  --entrypoint sh \
  pyrenex-risk-api:v0.1.0 \
  -c "pip install --quiet pytest httpx && pytest -v"

read -p "Press Enter to close this window..."
