from django.urls import path
from app.views.variant import VariantListView, VariantDetailView 
from app.views.reservation import ReservationView ,ReservationConfirmView, ReservationCancelView
from app.views.health import health_live, health_ready
from app.views import metrics, health
from app.views.admin import AdjustStockView, TriggerReconciliationView


urlpatterns = [
    path('api/variants/', VariantListView.as_view()),
    path('api/variants/<str:variant_id>/', VariantDetailView.as_view()),
    path('health/live/', health_live),
    path('health/ready/', health_ready),
    path('api/reservations/', ReservationView.as_view()),
    path('api/reservations/<str:reservation_id>/confirm/', ReservationConfirmView.as_view()),
    path('api/reservations/<str:reservation_id>/cancel/', ReservationCancelView.as_view()),
    path('metrics/', metrics.metrics_view),
    path('health/', health.health_check),
    path('admin/adjust-stock/', AdjustStockView.as_view()),
    path('admin/reconcile/', TriggerReconciliationView.as_view()),
 

]


    
