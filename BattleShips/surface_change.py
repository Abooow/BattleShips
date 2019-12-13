import pygame


def transform(image, scale, rotation) -> pygame.surface:
    ''' Transform a image

    :param image (surface): the image to change
    :param scale (tuple[int,int]): the new scale
    :param rotation (int): the new rotation

    :returns: a copy of the image but with a new transform
    :rtype: surface
    '''

    img_size = image.get_rect().size 

    new_image = image.copy()
    new_image = pygame.transform.scale(new_image, (img_size[0] * scale[0], img_size[1] * scale[1]))
    new_image = pygame.transform.rotate(new_image, rotation)
    
    return new_image


def colorize(image, new_color) -> pygame.surface:
    ''' Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of original).

    :param image (surface): surface to create a colorized copy of
    :param new_color (tuple[int,int,int]): RGB color to use (original alpha values are preserved)

    :return: new colorized Surface instance
    :rtype: surface
    '''
    image = image.copy()

    # zero out RGB values
    #image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    # add in new RGB values
    image.fill(new_color[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

    return image
