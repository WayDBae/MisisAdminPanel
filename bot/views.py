import traceback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bot.config.bot_config import Config

config = Config()


@csrf_exempt
def index(request):
    try:
        return JsonResponse({"message": "САЛАМАЛЕКСУС!"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# @csrf_exempt
# def handle_message(request, token):
#     if request.method == "POST" and token == TOKEN:
#         try:
#             json_string = request.body.decode("utf-8")
#             update = types.Update.de_json(json_string)
#             bot.process_new_updates([update])
#             return JsonResponse({"message": "Message processed successfully"})
#         except Exception as e:
#             return JsonResponse({"error": f"Error processing message: {str(e)}\n{traceback.format_exc()}"}, status=500)
#     return JsonResponse({"error": "Invalid request"}, status=400)
