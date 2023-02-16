import pygame
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        self.frames = {
			# magic
			'flame': import_folder('../Zelda-main/5 - level graphics/graphics/particles/flame/frames'),
			'aura': import_folder('../Zelda-main/5 - level graphics/graphics/particles/aura'),
			'heal': import_folder('../Zelda-main/5 - level graphics/graphics/particles/heal/frames'),

			# attacks
			'claw': import_folder('../Zelda-main/5 - level graphics/graphics/particles/claw'),
			'slash': import_folder('../Zelda-main/5 - level graphics/graphics/particles/slash'),
			'sparkle': import_folder('../Zelda-main/5 - level graphics/graphics/particles/sparkle'),
			'leaf_attack': import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf_attack'),
			'thunder': import_folder('../Zelda-main/5 - level graphics/graphics/particles/thunder'),

			# monster deaths
			'squid': import_folder('../Zelda-main/5 - level graphics/graphics/particles/smoke_orange'),
			'raccoon': import_folder('../Zelda-main/5 - level graphics/graphics/particles/raccoon'),
			'spirit': import_folder('../Zelda-main/5 - level graphics/graphics/particles/nova'),
			'bamboo': import_folder('../Zelda-main/5 - level graphics/graphics/particles/bamboo'),

			# leafs
			'leaf': (
				import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf1'),
				import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf2'),
				import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf3'),
				import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf4'),
				import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf5'),
				import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf6'),
				self.reflect_images(import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf1')),
				self.reflect_images(import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf2')),
				self.reflect_images(import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf3')),
				self.reflect_images(import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf4')),
				self.reflect_images(import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf5')),
				self.reflect_images(import_folder('../Zelda-main/5 - level graphics/graphics/particles/leaf6'))
				)
			}

    def reflect_images(self,frames):
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame,True,False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self,pos,groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos,animation_frames,groups)

    def create_particles(self,animation_type,pos,groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos,animation_frames,groups)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self): # run animation once then destroy sprite when done
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
