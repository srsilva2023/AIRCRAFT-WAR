from CODE.Constantes import SCREEN_WIDTH
from CODE.Enemy import Enemy
from CODE.EnemyShot import EnemyShot
from CODE.Entity import Entity
from CODE.PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_collision_screen(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
            if isinstance(ent, PlayerShot):
                if ent.rect.left >= SCREEN_WIDTH:
                    ent.health = 0
            if isinstance(ent, EnemyShot):
                if ent.rect.right <= 0:
                    ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_screen(entity1)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
