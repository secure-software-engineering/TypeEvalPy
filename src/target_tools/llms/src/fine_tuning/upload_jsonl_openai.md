export OPENAI_API_KEY=<key>

curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "purpose=fine-tune" \
  -F "file=@finetuning_set_v1.jsonl"


curl https://api.openai.com/v1/fine_tuning/jobs \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "training_file": "file-IGdlpi5pIEJTjB6ZYbPXlVBX",
  "model": "gpt-3.5-turbo-0613"
}'

curl https://api.openai.com/v1/fine_tuning/jobs \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "training_file": "file-IGdlpi5pIEJTjB6ZYbPXlVBX",
  "model": "gpt-3.5-turbo-1106"
}'
