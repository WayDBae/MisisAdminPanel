import traceback
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from bot.config.bot_config import Config

config = Config()


@require_http_methods(["GET", "POST"])
@csrf_exempt
def index(request):
        return HttpResponse("САЛАМАЛЕКСУС! Добро пожаловать в Админ-панель Расписаний МИСиС!")


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
