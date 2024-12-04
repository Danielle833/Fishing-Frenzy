import pygame, random, time
from sys import exit
from Fish import *
from pygame import mixer
pygame.init()
mixer.init()


# Title text
title_font = pygame.font.Font("Retro Gaming.ttf", 75)
title_surface = title_font.render('FISHING FRENZY', False, 'peachpuff4')
title_rect = title_surface.get_rect(midtop=(400, 60))

enter_font = pygame.font.Font("Retro Gaming.ttf", 50)
enter_surface = enter_font.render('Press [Enter] to Begin', False, 'grey29')
enter_rect = enter_surface.get_rect(midbottom=(400, 350))


# Various variables
enter_key = 0
title_variable = True
fishing = False
inventory_open = False


# Backgrounds/other images
ocean_background = pygame.image.load("Images\\Miscellaneous\\Ocean-Background.png")
boat_graphic = pygame.image.load("Images\\Miscellaneous\\Boat.png")
bottom_bar = pygame.image.load("Images\\Miscellaneous\\Bottom-Bar.png")


def background_display():
    screen.blit(ocean_background, (0, 0))
    screen.blit(boat_graphic, (0, 0))
    screen.blit(bottom_bar, (0, 0))
    screen.blit(bar_surface, bar_rect)


# Fishing animation
fishing_rod_1 = pygame.image.load("Images\\Miscellaneous\\Fishing_Rod_1.png")
fishing_rod_2 = pygame.image.load("Images\\Miscellaneous\\Fishing_Rod_2.png")
fishing_rod_3 = pygame.image.load("Images\\Miscellaneous\\Fishing_Rod_3.png")
fishing_animation = [fishing_rod_1, fishing_rod_2, fishing_rod_3]


# Fish list
fish = ["Bass", "Yellowfin Tuna", "Red Drum", "Dolphinfish", "Sunfish", "Rainbow Trout", "Pike", "Shark", "Octopus", "Trash"]
fish_weighting = [10, 6, 8, 5, 8, 7, 10, 2, 1, 9]


# Functions
def go_fish():
    chosen_fish = random.choices(fish, weights = fish_weighting, k=1)
    return chosen_fish

fishing_timer_start = 2
fishing_timer_stop = 9
    
# Caught fish text
fish_text_font = pygame.font.Font("Retro Gaming.ttf", 20)


# Bar display
bar_font = pygame.font.Font("Retro Gaming.ttf", 25)
bar_surface = bar_font.render('[SPACE] to fish | [I] for inventory | [T] for store', False, 'lightsalmon4')
bar_rect = bar_surface.get_rect(midbottom=(400, 490))


# Inventory variables
player_inventory = {
    "bass amount":           0,
    "yellowfin tuna amount": 0,
    "red drum amount":       0,
    "dolphinfish amount":    0,
    "sunfish amount":        0,
    "rainbow trout amount":  0,
    "pike amount":           0,
    "shark amount":          0,
    "octopus amount":        0,
    "trash amount":          0
}

player_inventory_two = ["bass amount", "yellowfin tuna amount", "red drum amount", "dolphinfish amount", "sunfish amount", "rainbow trout amount", "pike amount", "shark amount", "octopus amount", "trash amount"]


# Selling
fish_price = {
    "bass price":            9,
    "yellowfin tuna price":  55,
    "red drum price":        24,
    "dolphinfish price":     68,
    "sunfish price":         41,
    "rainbow trout price":   36,
    "pike price":            11,
    "shark price":           86,
    "octopus price":         100,
    "trash price":           5
}

store_inventory = ["trash be-gone", "shark bait", "octopi bait", "faster fishing", "profit increaser", "multi-fish net"]
store_prices = {
    "trash be-gone":    85,
    "shark bait":       10,
    "octopi bait":      15,
    "faster fishing":   30,
    "profit increaser": 50,
    "multi-fish net":   100
}

money = 0
fish_costs = ["bass price", "yellowfin tuna price", "red drum price", "dolphinfish price", "sunfish price", "rainbow trout price","pike price", "shark price", "octopus price", "trash price"]

inventory_title_font = pygame.font.Font("Retro Gaming.ttf", 30)
inventory_title_surface = inventory_title_font.render('INVENTORY', False, 'chocolate4')
inventory_title_rect = inventory_title_surface.get_rect(midtop=(400, 30))

store_title_font = pygame.font.Font("Retro Gaming.ttf", 30)
store_title_surface = store_title_font.render('STORE', False, 'chocolate4')
store_title_rect = store_title_surface.get_rect(midtop=(400, 30))

money_font = pygame.font.Font("Retro Gaming.ttf", 20)


# Selection box in inventory variables
c = 51
d = 109

inventory_background = pygame.image.load("Images\\Miscellaneous\\Inventory-Background.png")
inventory_box = pygame.image.load("Images\\Miscellaneous\\Rectangle.png")
inventory_rectangle = inventory_box.get_rect(center=(c, d))

store_x_r = False
store_x_l = False
store_y_d = False
store_y_u = False

e = -223
f = -72

# e = 177
# f = 178

store_background = pygame.image.load("Images\\Miscellaneous\\Store-Background.png")
store_box = pygame.image.load("Images\\Miscellaneous\\Store-Rectangle.png")
store_rectangle = store_box.get_rect(center=(e, f))

inventory_x_r = False
inventory_x_l = False
inventory_y_d = False
inventory_y_u = False

# Other Various inventory stuff
inventory_text_font = pygame.font.Font("Retro Gaming.ttf", 17)

store_font = pygame.font.Font("Retro Gaming.ttf", 25)
store_surface = store_font.render('Press [S] to sell', False, 'chocolate4')
store_rect = store_surface.get_rect(midtop=(400, 65))

inventory_font = pygame.font.Font("Retro Gaming.ttf", 25)
inventory_surface = inventory_font.render('Press [S] to buy', False, 'chocolate4')
inventory_rect = inventory_surface.get_rect(midtop=(400, 65))

added_fish_amount = 1

selling = False
buying = False
fish_num = 0
store_num = 0


# Music
mixer.music.load("Ocean Audio.mp3")
pygame.mixer.music.play(-1)


# Set the screen dimensions
screen = pygame.display.set_mode((800, 500))

# Window caption and icon
pygame.display.set_caption("Fishing Frenzy")

window_icon = pygame.image.load("Images\\Fish\\Bass.png")
pygame.display.set_icon(window_icon)

# Maximum frame rate
clock = pygame.time.Clock()

# Inventory toggle
inventory_open = False
store_open = False


# Run the program in a continuous loop
run = True

while run:

    screen.fill((133, 181, 237))
    screen.blit(ocean_background, (0,0))

    # Get key inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                if title_variable == True:
                    enter_key = 1

            elif event.key == pygame.K_SPACE:
                if enter_key == 1 and inventory_open == False:
                    fishing = True

            elif event.key == pygame.K_i:
                if fishing == False and enter_key == 1 and store_open == False:
                    inventory_open = not inventory_open

            elif event.key == pygame.K_t:
                if fishing == False and enter_key == 1 and inventory_open == False:
                    store_open = not store_open

            elif event.key == pygame.K_RIGHT:
                if inventory_open == True:
                    store_x_r = True
                elif store_open == True:
                    inventory_x_r = True
            elif event.key == pygame.K_LEFT:
                if inventory_open == True:
                    store_x_l = True
                elif store_open == True:
                    inventory_x_l = True
            elif event.key == pygame.K_DOWN:
                if inventory_open == True:
                    store_y_d = True
                elif store_open == True:
                    inventory_y_d = True
            elif event.key == pygame.K_UP:
                if inventory_open == True:
                    store_y_u = True
                elif store_open == True:
                    inventory_y_u = True
            elif event.key == pygame.K_s:
                if inventory_open == True:
                    selling = True
                elif store_open == True:
                    buying = True


    # Title opening
    if title_variable == True and enter_key == 0:
        screen.blit(title_surface, title_rect)
        screen.blit(enter_surface, enter_rect)

    # Gets rid of opening title
    if enter_key == 1:
        background_display()

    # Fishing
    if fishing:

        # Fishing rod animation
        for frame in range(0, 3):
            background_display()
            screen.blit(fishing_animation[frame], (0, 0))
            pygame.display.update()

        # Random time
        fishing_timer = random.randrange(fishing_timer_start, fishing_timer_stop)
        time.sleep(fishing_timer)

        current_fish = go_fish()
        current_fish = str(current_fish).strip("[']")

        if current_fish == "Bass":
            screen.blit(bass_fish, (300, 40))
            player_inventory["bass amount"] += added_fish_amount
        elif current_fish == "Yellowfin Tuna":
            screen.blit(yellowfintuna_fish, (300, 40))
            player_inventory["yellowfin tuna amount"] += added_fish_amount
        elif current_fish == "Red Drum":
            screen.blit(reddrum_fish, (300, 40))
            player_inventory["red drum amount"] += added_fish_amount
        elif current_fish == "Dolphinfish":
            screen.blit(dolphinfish_fish, (300, 40))
            player_inventory["dolphinfish amount"] += added_fish_amount
        elif current_fish == "Sunfish":
            screen.blit(sunfish_fish, (300, 40))
            player_inventory["sunfish amount"] += added_fish_amount
        elif current_fish == "Rainbow Trout":
            screen.blit(rainbowtrout_fish, (300, 40))
            player_inventory["rainbow trout amount"] += added_fish_amount
        elif current_fish == "Pike":
            screen.blit(pike_fish, (300, 40))
            player_inventory["pike amount"] += added_fish_amount
        elif current_fish == "Shark":
            screen.blit(shark_fish, (300, 30))
            player_inventory["shark amount"] += added_fish_amount
        elif current_fish == "Octopus":
            screen.blit(octopus_fish, (300, 30))
            player_inventory["octopus amount"] += added_fish_amount
        elif current_fish == "Trash":
            screen.blit(trash_fish, (300, 45))
            player_inventory["trash amount"] += added_fish_amount

        fish_text_surface = fish_text_font.render('You caught ' + current_fish + "!", False, 'lightsalmon4')
        fish_text_rect = fish_text_surface.get_rect(midtop=(400, 20))

        screen.blit(fish_text_surface, fish_text_rect)
        pygame.display.update()

        time.sleep(1.25)

        fishing = False

    # Inventory
    if inventory_open == True:
        fishing = False
        screen.blit(inventory_background, (0, 0))
        screen.blit(inventory_title_surface, inventory_title_rect)
        screen.blit(store_surface, store_rect)

        # Important variables
        i = 0
        a = 148
        b = 148

        # Fish amount numbers
        for x in player_inventory_two:
            i = i + 1
            if i <= 5:
                inventory_fish_surface = inventory_text_font.render(str(player_inventory[x]), False, 'lightsalmon4')
                inventory_fish_rect = inventory_fish_surface.get_rect(topright=(a, 198))
                screen.blit(inventory_fish_surface, inventory_fish_rect)
                a = a + 147

            elif i > 5:
                inventory_fish_surface = inventory_text_font.render(str(player_inventory[x]), False, 'lightsalmon4')
                inventory_fish_rect = inventory_fish_surface.get_rect(topright=(b, 338))
                screen.blit(inventory_fish_surface, inventory_fish_rect)
                b = b + 147

        # Moving Rectangle
        if store_x_l == True:
            c -= 147
            store_x_l = False
            fish_num -= 1

        elif store_x_r == True:
            c += 147
            store_x_r = False
            fish_num += 1

        elif store_y_d == True:
            d += 140
            store_y_d = False
            fish_num += 5

        elif store_y_u == True:
            d -= 140
            store_y_u = False
            fish_num -= 5

        if c < 51:
            c += 147
            fish_num += 1
        elif c > 750:
            c -= 147
            fish_num -= 1

        if d < 109:
            d += 140
            fish_num += 5
        elif d > 250:
            d -= 140
            fish_num -= 5

        inventory_rectangle.x = c
        inventory_rectangle.y = d
        screen.blit(inventory_box, inventory_rectangle)

        # Selling
        if selling == True:
            current_selling = player_inventory_two[fish_num]
            current_price = fish_costs[fish_num]
            added_money = player_inventory[current_selling] * fish_price[current_price]
            money = money + added_money

            player_inventory[current_selling] = 0
            selling = False

        money_surface = money_font.render('$' + str(money), False, 'chocolate4')
        money_rect = money_surface.get_rect(topright=(735, 30))
        screen.blit(money_surface, money_rect)

    # Store
    elif store_open == True:
        fishing = False
        screen.blit(store_background, (0, 0))
        screen.blit(store_title_surface, store_title_rect)
        screen.blit(inventory_surface, inventory_rect)

        g = 236
        h = 236
        j = 0

        # Displaying the item costs
        for x in store_inventory:
            j += 1
            if j <= 3:
                if store_prices[x] == "N/A":
                    store_price_surface = inventory_text_font.render(store_prices[x], False, 'lightsalmon4')
                else:
                    store_price_surface = inventory_text_font.render(f"${store_prices[x]}", False, 'lightsalmon4')
                store_price_rect = store_price_surface.get_rect(topright=(g, 220))
                screen.blit(store_price_surface, store_price_rect)
                g += 223
            elif j > 3:
                if store_prices[x] == "N/A":
                    store_price_surface = inventory_text_font.render(store_prices[x], False, 'lightsalmon4')
                else:
                    store_price_surface = inventory_text_font.render(f"${store_prices[x]}", False, 'lightsalmon4')
                store_price_rect = store_price_surface.get_rect(topright=(h, 386))
                screen.blit(store_price_surface, store_price_rect)
                h += 223

        if inventory_x_l == True:
            e -= 223
            store_num -= 1
            inventory_x_l = False

        elif inventory_x_r == True:
            e += 223
            store_num += 1
            inventory_x_r = False

        elif inventory_y_d == True:
            f += 165
            store_num += 3
            inventory_y_d = False

        elif inventory_y_u == True:
            f -= 165
            store_num -= 3
            inventory_y_u = False

        if e < -223:
            e += 223
            store_num += 1
        elif e > 400:
            e -= 223
            store_num -= 1

        if f < -72:
            f += 165
            store_num += 3
        elif f > 250:
            f -= 165
            store_num -= 3

        store_rectangle.x = e
        store_rectangle.y = f
        screen.blit(store_box, store_rectangle)


        if buying == True:
            current_buying = store_inventory[store_num]
            current_price = store_prices[current_buying]

            if store_num == 0 and current_price!= "N/A" and money >= int(current_price):
                fish_weighting[9] = 1
                money -= current_price
                store_prices[current_buying] = "N/A"
            elif store_num == 1 and current_price!= "N/A" and money >= current_price:
                fish_weighting[7] = 5
                money -= current_price
                store_prices[current_buying] = "N/A"
            elif store_num == 2 and current_price!= "N/A" and money >= current_price:
                fish_weighting[8] = 4
                money -= current_price
                store_prices[current_buying] = "N/A"
            elif store_num == 3 and current_price!= "N/A" and money >= current_price:
                fishing_timer_start = 1
                fishing_timer_stop = 4
                money -= current_price
                store_prices[current_buying] = "N/A"

            elif store_num == 4 and current_price!= "N/A" and money >= current_price:
                for x in range(len(fish_costs)):
                    fish_price[fish_costs[x]] += 30
                money -= current_price
                store_prices[current_buying] = "N/A"

            elif store_num == 5 and current_price!= "N/A" and money >= current_price:
                added_fish_amount += 2
                money -= current_price
                store_prices[current_buying] = "N/A"


            buying = False


        money_surface = money_font.render('$' + str(money), False, 'chocolate4')
        money_rect = money_surface.get_rect(topright=(735, 30))
        screen.blit(money_surface, money_rect)

    # Maximum frame rate pt. 2
    clock.tick(60)

    # Refreshes the screen
    pygame.display.flip()


# Exits the game
pygame.quit()
exit()
