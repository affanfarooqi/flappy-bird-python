import sys, pygame as pg
from .settings import *
from .bird import Bird
from .pipe import PipePair

pg.init()
pg.display.set_caption("Flappy Bird – Pygame")

def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock  = pg.time.Clock()

    bird   = Bird(60, HEIGHT // 2)
    pipes  = []
    score  = 0
    font   = pg.font.SysFont(None, 48)
    SPAWNPIPE = pg.USEREVENT + 1
    pg.time.set_timer(SPAWNPIPE, PIPE_FREQ_MS)

    running = True
    while running:
        # ── Events ───────────────────────────────────────────────────────
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and event.key in (pg.K_SPACE, pg.K_UP):
                bird.flap()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                bird.flap()
            if event.type == SPAWNPIPE:
                pipes.append(PipePair(WIDTH))

        # ── Update ────────────────────────────────────────────────────
        bird.update()
        for p in pipes:
            p.update()

        # Remove off-screen pipes
        pipes = [p for p in pipes if not p.offscreen]

        # Check collisions
        for p in pipes:
            if bird.rect.collidelist(p.rects) != -1:
                running = False  # game over
            # scoring
            if not p.passed and p.x + PIPE_WIDTH < bird.pos.x:
                p.passed = True
                score += 1

        if bird.pos.y > HEIGHT or bird.pos.y < 0:
            running = False

        # ── Draw ─────────────────────────────────────────────────────
        screen.fill((245, 245, 245))
        bird.draw(screen)
        for p in pipes:
            p.draw(screen)
        # HUD
        txt = font.render(str(score), True, (0, 0, 0))
        screen.blit(txt, (WIDTH // 2 - txt.get_width() // 2, 20))

        pg.display.flip()
        clock.tick(FPS)

    # Game over screen
    game_over(screen, font, score)
    pg.quit()
    sys.exit()

def game_over(screen, font, score):
    screen.fill((245, 245, 245))
    msg = font.render(f"Game Over! Score: {score}", True, (200, 30, 30))
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2,
                      HEIGHT // 2 - msg.get_height() // 2))
    pg.display.flip()
    pg.time.wait(2500)

if __name__ == "__main__":
    main()
