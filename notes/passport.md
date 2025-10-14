# Passport 

Passport strategies diferrent by how it extract the params then process (validate) them.

Standard: Guard (extends AuthGuard('strategy-name')) -> trggier Strategy with canActivate function
Customized: Guard -> Guard(super.canActivate) -> Strategy -> Strategy(validate) -> Guard(after canActivate() codes - custom)

```typescript
@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {
    constructor(@Inject(CACHE_MANAGER) private cacheManager: Cache) {
        super();
    }

    async canActivate(context: ExecutionContext): Promise<boolean> {
        await super.canActivate(context);
        const request = context.switchToHttp().getRequest();
        const token = ExtractJwt.fromAuthHeaderAsBearerToken()(request);
        if (await this.cacheManager.get(token)) {
            throw new UnauthorizedException({ translate: 'error.unauthorized' });
        }
        return true;
    }
}
```

```typescript
@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
    constructor(private userService: UserService) {
        super({
            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
            ignoreExpiration: false,
            secretOrKey: env.JWT.SECRET
        });
    }

    async validate(payload: { id: string }): Promise<UserEntity> {
        const user = await this.userService.findByIdNotFail(payload.id);
        if (!user) {
            throw new UnauthorizedException({ translate: 'error.unauthorized' });
        }

        return user;
    }
}
```

✅ Timeline (in order)

canActivate() is called.
await super.canActivate(context) runs.
Inside this:
Passport extracts token
Verifies token
Calls JwtStrategy.validate(payload)
Attaches request.user
Back to your JwtAuthGuard → extra checks (like token blacklist).
If all good → true returned → controller executes.

## Customized Strategy

```typescript
class ShortTokenAuthentication extends Strategy {
    constructor(private queryKey: string) {
        super();
    }

    authenticate(req: any) {
        const shortToken = req.query[this.queryKey];

        if (!shortToken) {
            return this.fail(new UnauthorizedException({ translate: 'error.unauthorized' }), null);
        }

        req['shortToken'] = shortToken;
        this.success(req);
    }
}

@Injectable()
export class ShortTokenStrategy extends PassportStrategy(ShortTokenAuthentication, SHORT_TOKEN_STRATEGY) {
    constructor(
        private userService: UserService,
        @Inject(CACHE_MANAGER) private cacheManager: Cache
    ) {
        super('shortToken');
    }

    async validate(req: Request) {
        const token = req['shortToken'];

        if (!token) {
            throw new UnauthorizedException({ translate: 'error.unauthorized' });
        }

        const userId = await this.cacheManager.get<string>(token);
        if (!userId) {
            throw new UnauthorizedException({ translate: 'error.unauthorized' });
        }

        const user = await this.userService.findByIdNotFail(userId);
        if (!user) {
            throw new UnauthorizedException({ translate: 'error.unauthorized' });
        }

        return user;
    }
}
```
