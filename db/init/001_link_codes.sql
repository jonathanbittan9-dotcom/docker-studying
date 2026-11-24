CREATE TABLE IF NOT EXISTS link_codes (
    code TEXT PRIMARY KEY,
    web_user_id INTEGER NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at TIMESTAMPTZ NOT NULL DEFAULT now() + interval '10 minutes',
    discord_user_id BIGINT,
    guild_id BIGINT,
    used_at TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS link_codes_discord_user_idx ON link_codes (discord_user_id);
CREATE INDEX IF NOT EXISTS link_codes_guild_idx ON link_codes (guild_id);
