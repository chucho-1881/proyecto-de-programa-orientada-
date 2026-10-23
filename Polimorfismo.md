from abc import ABC, abstractmethod


class pasareladepago(ABC):

    @abstractmethod
    def cobrar(self, monto: float) -> bool:
        """Procesa el cobro y devuelve True si tiene éxito."""
        pass


class pasarelapaypal(pasareladepago):

    def cobrar(self, monto: float) -> bool:
        print("[PayPal] Conectando con la API de PayPal...")
        print(f"[PayPal] Cobrando el servicio con el monto de ${monto:.2f}...")
        return True


class pasarelastripe(pasareladepago):

    def cobrar(self, monto: float) -> bool:
        print("[Stripe] Conectando con la API de Stripe...")
        print(f"[Stripe] Cobrando el servicio con el monto de ${monto:.2f}...")
        return True


class serviciodecaja:

    def __init__(self, pasarela: pasareladepago) -> None:
        self.pasarela = pasarela

    def procesar_compra(self, monto: float) -> None:
        print("Servicio de caja: validando orden de compra...")
        exito = self.pasarela.cobrar(monto)

        if exito:
            print("Servicio de caja: transaccion correcta")
        else:
            print("Servicio de caja: la transaccion ha fallado.")


if __name__ == "__main__":

    print("--- Procesando el pago con PayPal ---")
    pasarela_paypal = pasarelapaypal()
    caja_con_paypal = serviciodecaja(pasarela_paypal)
    caja_con_paypal.procesar_compra(100.00)

    print()

    print("--- Procesando el pago con Stripe ---")
    pasarela_stripe = pasarelastripe()
    caja_con_stripe = serviciodecaja(pasarela_stripe)
    caja_con_stripe.procesar_compra(200.00)
    
