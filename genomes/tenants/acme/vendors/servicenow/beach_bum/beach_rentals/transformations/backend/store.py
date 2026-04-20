from typing import List, Optional
from datetime import datetime
from .models import BeachRental, BeachRentalCreate, BeachRentalUpdate

class BeachRentalStore:
    _rentals: List[BeachRental] = []
    _current_id: int = 1

    @classmethod
    def _generate_id(cls) -> str:
        result = str(cls._current_id)
        cls._current_id += 1
        return result

    def create(self, rental: BeachRentalCreate) -> BeachRental:
        rental_id = self._generate_id()
        now = datetime.utcnow()
        new_rental = BeachRental(
            sys_id=rental_id,
            rental_duration=rental.rental_duration,
            customer_name=rental.customer_name,
            rental_type=rental.rental_type,
            created_on=now,
            created_by="system",
            updated_on=now,
            updated_by="system"
        )
        self._rentals.append(new_rental)
        return new_rental

    def get_by_id(self, rental_id: str) -> Optional[BeachRental]:
        for rental in self._rentals:
            if rental.sys_id == rental_id:
                return rental
        return None

    def list_all(self) -> List[BeachRental]:
        return self._rentals

    def update(self, rental_id: str, rental_update: BeachRentalUpdate) -> BeachRental:
        rental = self.get_by_id(rental_id)
        if rental:
            if rental_update.rental_duration is not None:
                rental.rental_duration = rental_update.rental_duration
            if rental_update.rental_type is not None:
                rental.rental_type = rental_update.rental_type
            rental.updated_on = datetime.utcnow()
            rental.updated_by = "system"
            return rental
        raise ValueError("Rental not found")

    def delete(self, rental_id: str) -> None:
        self._rentals = [rental for rental in self._rentals if rental.sys_id != rental_id]

    def exists(self, rental_id: str) -> bool:
        return any(rental.sys_id == rental_id for rental in self._rentals)