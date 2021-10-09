import json
from urllib.parse import urlparse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from form_process.models import Form, FormResponse


@csrf_exempt
@require_http_methods(["POST"])
def FormSubmission(request):
    print(request.body)
    try:
        jsonBody = json.loads(request.body)
        form_record = Form.objects.get(id=jsonBody["id"])

        if form_record.whitelist_mode:
            if "HTTP_ORIGIN" in request.META:
                 o = urlparse(request.META["HTTP_ORIGIN"])
                #  print(o.netloc)
                #  print(form_record.whitelist_websites)
                 if o.netloc not in form_record.whitelist_websites:
                    return JsonResponse({
                        "success": False,
                        "message": "",
                        "error": "Website Not Whitelisted"
                        })
            else:
                return JsonResponse({
                    "success": False,
                    "message": "",
                    "error": "Use a secure browser"
                    })


        if not form_record.is_active:
            return JsonResponse({
                "success": False,
                "message": "",
                "error": "Form Submission Closed"
                })
        


        keys_in_form = list(jsonBody["data"].keys())
        form_record_keys = list(form_record.variables)
        isNeedToUpdateDatabase = False
        for key in keys_in_form:
            if key not in form_record_keys:
                form_record_keys.append(key)
                isNeedToUpdateDatabase = True

        if isNeedToUpdateDatabase:
            form_record.variables = form_record_keys
            form_record.save()

        FormResponse.objects.create(
            form=form_record,
            data_json=jsonBody["data"]
        )

        return JsonResponse({
            "success": True,
            "message": "Form Submitted Successfully",
            "error": ""
        })
    except:
        return JsonResponse({
            "success": False,
            "message": "",
            "error": "Form Submission Failed"
        })
