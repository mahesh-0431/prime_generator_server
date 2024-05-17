from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PrimeExecution
from .prime_generator import prime,mahi
import time

@api_view(['GET'])
def generate_primes(request):
    start = int(request.GET.get('start'))
    end = int(request.GET.get('end'))
    strategy = request.GET.get('strategy', 'prime')

    start_time = time.time()

    if strategy == 'prime':
        res = prime(start, end)
    elif strategy == 'mahi':
        res = mahi(start, end)
    else:
        return Response({"error": "Invalid strategy"}, status=400)

    end_time = time.time()
    time_elapsed = end_time - start_time

    record = PrimeExecution.objects.create(
        start=start,
        end=end,
        elapsed=time_elapsed,
        algorithm=strategy,
        num_primes=len(res)
    )

    return Response({"primes": res,"time":time_elapsed,"length":len(res)})

