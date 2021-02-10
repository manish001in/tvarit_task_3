# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import json

@csrf_exempt
def number_sum(request):
    if request.method == "PUT":

        no_list = json.loads(request.body)

        if len(no_list)!=3:
            return JsonResponse({'status': 400, "error": "Exactly 3 numbers are required"})
        else:
            sum = 0
            for i in no_list:
                try:
                    i = int(i)
                    if i==15 or i==16:
                        sum += int(i)
                    elif i>=13 and i<=19:
                        pass
                    else:
                        sum += int(i)

                except ValueError as e:
                    return JsonResponse({'status': 400, "error": "All inputs must be numeric"})
                    
            return JsonResponse({'status': 200, "result": sum})

    else:
        return JsonResponse({'status': 500, "error": "Invalid request method"})